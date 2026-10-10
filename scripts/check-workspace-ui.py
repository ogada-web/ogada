#!/usr/bin/env python3
"""Read-only browser audit of every visible menu for four preview roles.

Run with .venv/bin/python scripts/check-workspace-ui.py.
Credentials stay in .venv/phone-preview/settings.json; only local preview origins
are permitted. Reports and screenshots are written under /tmp.
"""
import asyncio,json,os,time,re
from pathlib import Path
from urllib.parse import urlsplit
os.environ['TMPDIR']='/dev/shm/ogada-mobile-ui-check'
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1];STATE=ROOT/'.venv/phone-preview';S=json.loads((STATE/'settings.json').read_text());OUT=Path(os.environ.get('OGADA_UI_AUDIT_DIR', '/tmp/ogada-workspace-ui-audit'));OUT.mkdir(exist_ok=True);BASE=os.environ.get('OGADA_UI_AUDIT_BASE', 'http://127.0.0.1:4174');assert urlsplit(BASE).hostname in {'127.0.0.1','localhost'}, 'Use a local preview origin'
METRICS='''() => {
 const main=document.querySelector('.ds-main');if(!main)return {missingMain:true};
 const r=main.getBoundingClientRect();
 const outside=[...main.querySelectorAll('.ds-card,.ds-field,.ds-form-row,.ds-form-grid,.ds-action-bar,.ds-datetime-field-row')].filter(e=>{const b=e.getBoundingClientRect();return b.width>0&&(b.right>r.right+2||b.left<r.left-2)}).map(e=>({class:e.className,width:Math.round(e.getBoundingClientRect().width)}));
 const rawLinks=[...main.querySelectorAll('a')].filter(e=>{const b=e.getBoundingClientRect(),s=getComputedStyle(e);return b.width>0&&(s.color==='rgb(0, 0, 238)'||s.color==='rgb(85, 26, 139)');}).map(e=>({text:e.textContent.trim().slice(0,70),href:e.getAttribute('href'),class:e.className,parent:e.parentElement.tagName+' '+e.parentElement.className}));
 const internal=[...main.querySelectorAll('h1,h2,h3,h4,p,summary')].filter(e=>/\\b(?:G\\d+[a-z]?|US-[A-Z][A-Z0-9_-]*|BNK-\\d+|L\\d+_M\\d+|FAQ\\d+)|케어포|이지케어|care-scoped|API 경로|PoC|lifecycle/.test(e.textContent)).map(e=>e.textContent.trim().slice(0,200));
 return {title:main.querySelector('h1')?.textContent,mainOverflow:main.scrollWidth-main.clientWidth,outside:outside.slice(0,10),rawLinks:rawLinks.slice(0,12),internalCopy:internal.slice(0,15),windowScrollY:scrollY,headerTop:document.querySelector('.ds-topbar')?.getBoundingClientRect().top,spinners:main.querySelectorAll('.ds-spinner,.ds-page-loading').length};
}'''
async def login(browser,width,email='test3@test.com'):
 context=await browser.new_context(viewport={'width':width,'height':900},is_mobile=width<=768,has_touch=width<=768)
 page=await context.new_page();await page.goto(BASE+'/login');await page.get_by_label('이메일',exact=False).fill(email);await page.get_by_label('비밀번호',exact=False).fill(S['PREVIEW_PASSWORD']);await page.get_by_role('button',name='로그인',exact=True).click();await page.wait_for_url('**'+('/platform' if email.startswith('test5') else '/dashboard' if email.startswith('test1') or email.startswith('test2') else '/dashboard/hq'),timeout=30000)
 return context,page
async def run():
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/home/ubuntu/.cache/ms-playwright/chromium-1234/chrome-linux/chrome',args=['--no-sandbox'])
  context,page=await login(browser,1440)
  paths=await page.locator('.ds-sidenav a').evaluate_all('(nodes)=>nodes.map(e=>e.getAttribute("href"))')
  paths=list(dict.fromkeys(paths));paths+=['/clients/new','/transport/runs/new','/nursing/service/reports/total','/nursing/service/reports/hospital-visits','/nursing/service/reports/medication-delivery']
  client='d1000001-0001-4000-8000-000000000001';paths += [f'/clients/{client}',f'/clients/{client}/edit',f'/clients/{client}/files',f'/clients/{client}/care-plan-form']
  fixture=json.loads((STATE/'restored-transport-runs.json').read_text());paths.append('/transport/runs/'+fixture['runIds'][0]);paths=list(dict.fromkeys(paths))
  rolePaths={'test3@test.com':paths}
  for email in ['test1@test.com','test2@test.com']:
   ctx, rolePage=await login(browser,1440,email)
   rolePaths[email]=list(dict.fromkeys(await rolePage.locator('.ds-sidenav a').evaluate_all('(nodes)=>nodes.map(e=>e.getAttribute("href"))')))
   await ctx.close()
  await context.close();results=[];queue=asyncio.Queue()
  for width in [1440,390]:
   for email,rolePathsList in rolePaths.items():
    for path in rolePathsList:queue.put_nowait((width,path,email))
   queue.put_nowait((width,'/platform','test5@test.com'))
  total=queue.qsize();print('Audit combinations:',total,flush=True)
  async def worker(index):
   contexts={}
   while not queue.empty():
    try:width,path,email=queue.get_nowait()
    except asyncio.QueueEmpty:break
    key=(width,email)
    if key not in contexts:contexts[key]=await login(browser,width,email)
    ctx,page=contexts[key];fails=[];errors=[];pending=set()
    def response(r):
     if '/api/v1/' in r.url and r.status>=400:fails.append({'path':urlsplit(r.url).path,'status':r.status})
    def err(e):errors.append(str(e)[:250])
    def start(r):
     if '/api/v1/' in r.url:pending.add(r)
    def end(r):pending.discard(r)
    page.on('response',response);page.on('pageerror',err);page.on('request',start);page.on('requestfinished',end);page.on('requestfailed',end)
    row={'width':width,'path':path,'role':email.split('@')[0]}
    try:
     await page.evaluate('''path => {
      const link=[...document.querySelectorAll('.ds-sidenav a')].find(e=>e.getAttribute('href')===path);
      if(link){link.click();return;}
      history.pushState({...history.state,idx:(history.state?.idx||0)+1,key:'ui-audit-'+Math.random()},'',path);
      window.dispatchEvent(new PopStateEvent('popstate',{state:history.state}));
     }''',path)
     await page.locator('.ds-page-loading--route').wait_for(state='hidden',timeout=20000)
     await page.wait_for_timeout(400)
     for _ in range(20):
      if not pending:break
      await page.wait_for_timeout(150)
     await page.wait_for_timeout(150)
     row.update(await page.evaluate(METRICS));row['actualPath']=urlsplit(page.url).path;row['apiFailures']=[failure for failure in fails if not (failure['status']==404 and re.search(r'/clients/[0-9a-f-]+/care-plan-forms/\d{4}$',failure['path']))];row['emptyPlanRequests']=[failure for failure in fails if failure not in row['apiFailures']];row['errors']=errors
     name=str(width)+'-'+re.sub(r'[^a-zA-Z0-9_-]','_',path.strip('/'))+'.png';await page.screenshot(path=str(OUT/name));row['image']=name
    except Exception as e:row['auditError']=type(e).__name__+': '+str(e)[:200]
    for event,fn in [('response',response),('pageerror',err),('request',start),('requestfinished',end),('requestfailed',end)]:page.remove_listener(event,fn)
    results.append(row);queue.task_done()
    if len(results)%20==0:print('Checked',len(results),'/',total,flush=True)
   for ctx,_ in contexts.values():await ctx.close()
  await asyncio.gather(*(worker(i) for i in range(3)))
  await browser.close();(OUT/'audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
  issues=[r for r in results if r.get('missingMain') or r.get('mainOverflow',0)>1 or r.get('outside') or r.get('rawLinks') or r.get('internalCopy') or r.get('apiFailures') or r.get('errors') or r.get('auditError')]
  print('Completed',len(results),'checks; pages with findings',len(issues),flush=True)
  print('API findings:',json.dumps([{'path':r['path'],'failures':r.get('apiFailures'),'auditError':r.get('auditError')} for r in issues if r.get('apiFailures') or r.get('auditError')],ensure_ascii=False),flush=True)
asyncio.run(run())
