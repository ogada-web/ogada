#!/usr/bin/env python3
"""Check real compiled transport layouts with local demo credentials and Playwright.

Run against a local compiled demo server after building the frontend. No data is
saved: selecting clients and moving route stops only changes browser state.
"""
import argparse
import json
import os
from pathlib import Path
from urllib.parse import urlsplit

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
CHROMIUM = Path('/home/ubuntu/.cache/ms-playwright/chromium-1234/chrome-linux/chrome')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', default='http://127.0.0.1:4174')
    parser.add_argument('--widths', nargs='+', type=int, default=[320, 360, 390, 430, 768, 1440])
    parser.add_argument('--out', type=Path, default=Path('/tmp/ogada-transport-mobile-layout'))
    args = parser.parse_args()
    assert urlsplit(args.base).hostname in {'localhost', '127.0.0.1'}, 'Credentials must stay local'
    settings = json.loads((ROOT / '.venv/phone-preview/settings.json').read_text())
    fixture = json.loads((ROOT / '.venv/phone-preview/restored-transport-runs.json').read_text())
    args.out.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault('TMPDIR', '/dev/shm/ogada-mobile-ui-check')
    results = []

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=str(CHROMIUM), args=['--no-sandbox'])
        for width in args.widths:
            mobile = width <= 768
            page = browser.new_page(viewport={'width': width, 'height': 844}, is_mobile=mobile, has_touch=mobile)
            errors = []
            page.on('pageerror', lambda error: errors.append(str(error)))
            page.goto(args.base + '/login')
            page.get_by_label('이메일', exact=False).fill(settings['PREVIEW_EMAIL'])
            page.get_by_label('비밀번호', exact=False).fill(settings['PREVIEW_PASSWORD'])
            page.get_by_role('button', name='로그인', exact=True).click()
            page.wait_for_url('**/dashboard/hq')
            sheet = args.base + '/transport/shuttle-sheet?runDate=' + fixture['runDate'] + '&direction=PICKUP'
            page.goto(sheet)
            page.get_by_role('link', name='송영표 편집', exact=True).first.wait_for(timeout=40000)
            page.wait_for_function("document.querySelectorAll('.ds-shuttle-stack__passenger-card').length === 10")
            if mobile:
                assert_sheet_fit(page)
                # Larger text must not clip late arrival labels or passenger cards.
                page.add_style_tag(content='html { font-size: 20px; }')
                assert_sheet_fit(page)
            else:
                assert page.locator('.ds-shuttle-stack').evaluate(
                    '(e) => getComputedStyle(e).gridTemplateColumns.split(" ").length'
                ) == 2, 'Desktop vehicle columns changed'
            page.locator('.ds-shuttle-stack__column').last.scroll_into_view_if_needed()
            page.screenshot(path=str(args.out / f'sheet-{width}.png'))
            page.get_by_role('link', name='송영표 편집', exact=True).first.click()
            page.get_by_role('heading', name='경로 지도', exact=True).wait_for(timeout=30000)
            if mobile:
                assert_stops_fit(page)
            page.locator('.ds-transport-route-split__stops').scroll_into_view_if_needed()
            page.screenshot(path=str(args.out / f'editor-{width}.png'))
            page.get_by_role('link', name='송영표로', exact=True).click()
            page.get_by_role('link', name='송영표 작성', exact=True).click()
            choices = page.locator('input[type=checkbox][id^=transport-client-]')
            choices.first.wait_for(timeout=20000)
            choices.nth(0).check()
            choices.nth(1).check()
            page.wait_for_function("document.querySelectorAll('.ds-transport-stop').length >= 2")
            if mobile:
                assert_stops_fit(page)
            assert not errors, errors
            results.append({'width': width, 'sheet': 'PASS', 'existingEditor': 'PASS', 'newEditor': 'PASS'})
            page.close()
        browser.close()
    print(json.dumps(results, ensure_ascii=False))


def assert_sheet_fit(page):
    failures = page.evaluate('''() => {
        const scroll = document.querySelector('.ds-shuttle-grid__scroll');
        const bounds = scroll.getBoundingClientRect();
        const columns = [...document.querySelectorAll('.ds-shuttle-stack__column')];
        const errors = columns.filter(e => {
            const r=e.getBoundingClientRect(); return r.left < bounds.left-1 || r.right > bounds.right+1;
        }).map(() => 'Vehicle column clipped');
        const rows = document.querySelectorAll('.ds-shuttle-stack__passenger-card');
        for (const row of rows) {
            if(row.scrollHeight > row.clientHeight+1) errors.push('Passenger card clips text');
            for (const label of row.querySelectorAll('strong,span')) {
                const range=document.createRange();range.selectNodeContents(label);
                for(const rect of range.getClientRects()) {
                    const card=row.getBoundingClientRect();
                    if(rect.right > card.right+1 || rect.left < card.left-1) errors.push('Passenger text clipped');
                }
            }
        }
        for(const button of document.querySelectorAll('.ds-transport-run-view-toggle .ds-btn')) {
            const r=button.getBoundingClientRect();
            if(r.right > bounds.right+1 || r.left < bounds.left-1) errors.push('Toolbar clipped');
        }
        return errors;
    }''')
    assert not failures, failures


def assert_stops_fit(page):
    failures = page.evaluate('''() => {
        const errors=[];
        for(const details of document.querySelectorAll('.ds-transport-stop__details')) {
            if(details.clientWidth < 120) errors.push('Address column too narrow');
        }
        for(const stop of document.querySelectorAll('.ds-transport-stop')) {
            if(stop.scrollWidth > stop.clientWidth+1) errors.push('Stop row overflows');
            for(const button of stop.querySelectorAll('.ds-transport-stop__actions button')) {
                const r=button.getBoundingClientRect();
                if(r.width<44 || r.height<44) errors.push('Route control too small for touch');
            }
        }
        const main=document.querySelector('.ds-main');
        if(main.scrollWidth > main.clientWidth+1) errors.push('Page overflows');
        return errors;
    }''')
    assert not failures, failures


if __name__ == '__main__':
    main()
