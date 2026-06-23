var main_nav_item = [
	{ //########################################################################################

		menuNo	: '1',
		menuName: '직원',
		item	:[
			{ name:'검색/관리/등록',		width:'1200',	height:'700',	action:'link',	url:'worker-list' },
			{ name:'문자 보내기 & 받은쪽지 <i id="newMsgCnt" class="messageOn"></i>',		width:'1200',	height:'600',	action:'dialog',	url:'mobile-sendW', attr:'', depth:'1', access_set:true },
			{ name:'-' },
			{ name:'연간 관리 현황',		width:'1100',	height:'700',	action:'link',	url:'worker-b100', attr:'' },
			{ name:'연차휴가',			width:'1100',	height:'700',	action:'link',	url:'worker-b100#tab0', depth:'1', attr:'' },
			{ name:'건강검진',			width:'1100',	height:'700',	action:'link',	url:'worker-b100#tab1', depth:'1', attr:'' },
			{ name:'직무교육',			width:'1100',	height:'700',	action:'link',	url:'worker-b100#tab2', depth:'1', attr:'' },
			{ name:'보수교육 현황',		width:'1100',	height:'700',	action:'link',	url:'worker-b100#tab3', depth:'1', attr:'' },
			{ name:'교육이수 현황',		width:'1100',	height:'700',	action:'link',	url:'worker-b100#tab4', depth:'1', attr:'' },
			{ name:'-' },
			{ name:'직원 서류작성 현황',		width:'1180',	height:'700',	action:'link',	url:'worker-workerDoc', attr:'new' },
			{ name:'요양보호사 상담일지',		width:'1200',	height:'700',	action:'link',		url:'worker-workerDoc#tab0', attr:'' , depth:'1' },
			{ name:'관리이력 검색 및 출력',	width:'800',	height:'700',	action:'dialog',	url:'worker-g03' },
			{ name:'직원 집계 및 현황',		width:'800',	height:'700',	action:'dialog',	url:'worker-g01', attr:''  },
			{ name:'일일 방문일정',		width:'800',	height:'700',	action:'dialog',	url:'worker-g02' },
			{ name:'-' },
			//{ name:'배상책임보험 관리',		width:'900',	height:'700',	action:'link',		url:'/baseData/liability_insurance.html', attr:'',	old:true },
			{ name:'배상책임보험 관리',		width:'900',	height:'700',	action:'link',		url:'worker-insurance', attr:'' },
			{ name:'코로나19 예방접종 현황',	width:'700',	height:'700',	action:'dialog',	url:'worker-g04', attr:'' },
			{ name:'-' },
			{ name:'직원 출퇴근부/근무일지',	width:'840',	height:'780',	action:'link',	url:'worker-timesheet3', attr:'' },
			{ name:'-' },
			{ name:'급여기초자료 설정',		width:'1200',	height:'780',	action:'dialog',	url:'wAllowance-awData#tab0', attr:'' },
			{ name:'-' },
			{ name:'앱 초대하기 (접속키 발송 →요보사)',			width:'1200',	height:'700',	action:'dialog',		url:'mobile-aKey#tabs-mobile-app_aKey-01', attr:'' },
			{ name:'앱 공지사항 (→요보사)',	width:'1200',	height:'700',	action:'dialog',		url:'mobile-notice#tabs-mobile-app-notice-01', attr:'' },
			{ name:'-', attr:'dev' },
			{ name:'직원정보 검증 및 수정',	width:'1180',	height:'700',	action:'dialog',	url:'worker-check.data.w4c', attr:'DEV' },
			{ name:'모바일 요청 확인',		width:'1180',	height:'700',	action:'dialog',	url:'mobile-apply', attr:'DEV' },
			//{ name:'앱 초대하기 (초대장 발송 →요보사)',			width:'1200',	height:'700',	action:'dialog',		url:'mobile-aKey2#tabs-mobile-app_aKey-01', attr:'DEV' },
			//{ name:'상근직 출퇴근부-old',			width:'840',	height:'780',	action:'dialog',	url:'worker-timesheet', attr:'DEV' }
			//{ name:'배상책임보험-news',			width:'1100',	height:'700',	action:'link',	url:'worker-insurance', attr:'dev' }
		],
	},{ //########################################################################################

		menuNo	: '2',
		menuName: '수급자',
		item	:[
			{ name: '검색/관리/등록',		width:'1200',	height:'700',	action:'link',		url:'patient-list',  attr:'' },
			{ name:'문자 보내기',			width:'1200',	height:'600',	action:'dialog',	url:'mobile-sendP', attr:'', depth:'1', access_set:true },
			{ name:'-' },
			{ name:'정기욕구평가 현황',		width:'1100',	height:'700',	action:'link',	url:'patient-b100', attr:'' },
			//{ name:'항목별 현황',			width:'1100',	height:'700',	action:'link',	url:'patient-b100#tab0', depth:'1', attr:'' },
			//{ name:'월별 현황',			width:'1100',	height:'700',	action:'link',	url:'patient-b100#tab1', depth:'1', attr:'' },
			//{ name:'월-항목별-수급자',		width:'1100',	height:'700',	action:'link',	url:'patient-b100#tab2', depth:'1', attr:'' },
			{ name:'수급자 서류작성 현황',	width:'1200',	height:'700',	action:'link',		url:'patient-patientDoc' , attr:'new'},
			{ name:'상태변화기록지',			width:'1200',	height:'700',	action:'link',		url:'patient-patientDoc#tab0', attr:'' , depth:'1' },
			{ name:'상담일지',			    width:'1200',	height:'700',	action:'link',		url:'patient-patientDoc#tab1', attr:'' , depth:'1' },
			{ name:'직원변경 상담일지',		width:'1200',	height:'700',	action:'link',		url:'patient-patientDoc#tab2', attr:'' , depth:'1' },
			{ name:'-' },
			{ name:'관리이력 검색 및 출력',	width:'900',	height:'700',	action:'dialog',	url:'patient-g03', attr:''},
			{ name:'수급자 집계 및 현황',	width:'800',	height:'700',	action:'dialog',	url:'patient-g01', attr:''},
			{ name:'일일 방문일정',		width:'800',	height:'700',	action:'dialog',	url:'patient-g02', attr:'' },
			{ name:'코로나19 예방접종 현황',	width:'800', height:'700', action:'dialog',	url:'patient-g04', attr:'' },
			{ name:'-' },
			{ name:'앱 초대하기 (접속키 발송 →수급자)',			width:'1200',	height:'700',	action:'dialog',		url:'mobile-aKey#tabs-mobile-app_aKey-02', attr:'' },
			{ name:'앱 공지사항 (→수급자)',	width:'1200',	height:'700',	action:'dialog',		url:'mobile-notice#tabs-mobile-app-notice-02', attr:'' },
			{ name:'-' },
			{ name:'본인부담금 현금영수증',	width:'1200',	height:'700',	action:'link',		url:'receipt-list', attr:'' },
			{ name:'발행 내역',			width:'1200',	height:'700',	action:'link',		url:'receipt-list#tab0', depth:'1' },
			{ name:'발행 정보관리',			width:'1200',	height:'700',	action:'link',		url:'receipt-list#tab1', depth:'1' },
			{ name:'변경사유 조회',			width:'1200',	height:'700',	action:'link',		url:'change-list', attr:'DEV' }
		],
	},{ //########################################################################################

		menuNo	: '3',
		menuName: '방문일정',
		item	:[
			{ name:'수급자-일정관리',		action:'popup',	url:'/schedule_plan/', script:'javascript:ScheduleManager("","")'},
			{ name:'관리자-일정관리',		action:'popup',	url:'/social_worker/schedule.html', script:'javascript:social_ScheduleManager()' },
			{ name:'-' },
			{ name:'일정표 출력 및 문자발송',		width:'1100',	height:'700',	action:'link',	url:'schedule-p100', attr:'' },
			{ name:'수급자 일정표(제공기록지)',		width:'1100',	height:'700',	action:'link',	url:'schedule-p100#tab0', depth:'1', attr:'' },
			{ name:'요양보호사 일정표(근무현황표)',	width:'1100',	height:'700',	action:'link',	url:'schedule-p100#tab1', depth:'1', attr:'' },
			{ name:'-' },
			{ name:'연간 서비스제공 명단',			width:'900',	height:'700',	action:'link',	url:'schedule-p300', attr:'' },
			{ name:'수급자',						width:'900',	height:'700',	action:'link',	url:'schedule-p300#tab0', depth:'1', attr:'' },
			{ name:'요양보호사',					width:'900',	height:'700',	action:'link',	url:'schedule-p300#tab1', depth:'1', attr:'' },
			{ name:'-' },
			{ name:'방문현황(일일, 주간, 월간)',	width:'1100',	height:'700',	action:'link',	url:'schedule-p500', attr:'' },

			{ name:'중증수당 일정 집계',	width:'1000',	height:'700',	action:'popup',	url:'/PU.ez?PGID=schedule-s100',old:true },
			{ name:'요양보호사 기준',	width:'1000',	height:'700',	action:'popup',	url:'/PU.ez?PGID=schedule-s100#tab0', depth:'1',old:true },
			{ name:'수급자 기준',		width:'1000',	height:'700',	action:'popup',	url:'/PU.ez?PGID=schedule-s100#tab1', depth:'1',old:true },
		
			{ name:'방문현황(일일, 주간, 월간)',	width:'900',	height:'700',	old:true,	action:'link', url:'/schedule_print/statusTable.html', attr:'DEV' }
		],
	},{ //########################################################################################

		menuNo	: '4',
		menuName: 'RFID점검',
		item	:[
			{ name:'RFID태그 내역 ↔ 공단계획 비교',	width:'1300',	height:'900',	action:'link',	url:'schedule-rfid', attr:'' },
			/*{ name:'RFID태그 내역 ↔ 공단계획 비교',	action:'popup',	url:'/schedule_plan/rfid_compare.html', script:'javascript:RfidTagCompare("","");' },*/
			{ name:'-' },
			{ name:'일정확정',					width:'1300',	height:'700',	action:'link',	url:'schedule-fix', attr:'' }
		],
	},{ //########################################################################################

		menuNo	: '5',
		menuName: '본인부담',
		item	:[
			{ name:'청구내역 및 명세서',		width:'1100',	height:'700',	action:'link',	url:'pAmt-a100', attr:'' },
			{ name:'전체(합산)',			    width:'1100',	height:'700',	action:'link',	url:'pAmt-a100#tab0', depth:'1', attr:'' },
			{ name:'방문요양',				width:'1100',	height:'700',	action:'link',	url:'pAmt-a100#tab1', depth:'1', attr:'' },
			{ name:'방문목욕',				width:'1100',	height:'700',	action:'link',	url:'pAmt-a100#tab2', depth:'1', attr:'' },
			{ name:'방문간호',				width:'1100',	height:'700',	action:'link',	url:'pAmt-a100#tab3', depth:'1', attr:'' },
			{ name:'-' },
			{ name:'납부내역',				width:'1100',	height:'700',	action:'link',	url:'pAmt-a200', attr:'' },
			{ name:'월간 수납내역',			width:'1100',	height:'700',	action:'link',	url:'pAmt-a200#tab0', depth:'1', attr:'' },			
			{ name:'연간 수납내역',			width:'1100',	height:'700',	action:'link',	url:'pAmt-a200#tab1', depth:'1', attr:'' },
			{ name:'장기요양급여비 납부확인서',	width:'1100',	height:'700',	action:'link',	url:'pAmt-a200#tab2', depth:'1', attr:'' },
			{ name:'-' },
			{ name:'미납내역',				width:'1100',	height:'700',	action:'link',	url:'pAmt-a400', attr:'' },
			{ name:'청구월별 미납금',			width:'1100',	height:'700',	action:'link',	url:'pAmt-a400#tab0', depth:'1', attr:'' },
			{ name:'수급자별 누적 미납금',		width:'1100',	height:'700',	action:'link',	url:'pAmt-a400#tab1', depth:'1', attr:'' },
			{ name:'청구내역 및 명세서(w4c)',		width:'1100',	height:'700',	action:'link',	url:'pAmt-a100.w4c', attr:'dev' }
		],
	},{ //########################################################################################

		menuNo	: '6',
		menuName: '직원급여',
		item	:[
			{ name:'급여명세서 작성 및 관리',	action:'popup', url:'/worker_allowance_V6/load.ez', script:'javascript:pop_WAV6()' },
			{ name:'-' },
			{ name:'연간 급여 및 사회보험 누계',	width:'900',	height:'700',	action:'link',	url:'wAllowance-a100', attr:'' },
			{ name:'월별 합산',				width:'900',	height:'700',	action:'link',	url:'wAllowance-a100#tab0', depth:'1', attr:'' },
			{ name:'직원별 합산',				width:'900',	height:'700',	action:'link',	url:'wAllowance-a100#tab1', depth:'1', attr:'' },
			{ name:'-' },
			{ name:'퇴직금 적립',				width:'900',	height:'700',	action:'link',	url:'wAllowance-severance' },
			// { name:'퇴직금 적립',			width:'900',	height:'700',	old:true,	action:'link',	url:'/worker_allowance_V5/severance_pay.html' },
			// { name:'퇴직금 적립',			width:'900',	height:'700',	action:'popup',	url:'', script:'javascript:alert("6월 20일 13:00시에 개선된 퇴직금 관리페이지가 오픈될 예정입니다.<br>이용에 불편을드려 죄송합니다.")' },
			{ name:'-' },
			{ name:'인건비 지급 비율 참고자료',		width:'900',	height:'700',	old:false,	action:'link',	url:'wAllowance-payrollcost' },
			// { name:'인건비 지급 비율 참고자료',	width:'900',	height:'700',	old:true,	action:'link',	url:'/worker_allowance_V5/payroll_cost_rate.html' },
			{ name:'-' },
			{ name:'급여기초자료 설정',	width:'1200',	height:'760',	action:'dialog',	url:'wAllowance-awData', attr:'' },
			{ name:'수당산정방식 및 분개값',	width:'1200',	height:'760',	action:'dialog',	url:'wAllowance-awData#tab0', depth:'1', attr:'' },
			{ name:'사회보험 현황 관리',	width:'1200',	height:'760',	action:'dialog',	url:'wAllowance-awData#tab1', depth:'1', attr:'' },
			{ name:'월급제 수당 관리',	width:'1200',	height:'760',	action:'dialog',	url:'wAllowance-awData#tab2', depth:'1', attr:'' },
			{ name:'-' },
			{ name:'목욕/간호 건별수당 설정',	width:'700',	height:'500',	action:'dialog',	url:'wAllowance-a200', attr:'' },
			{ name:'-' },
			{ name:'인건비 지급비율 DEV-han',				width:'900',	height:'700',	old:false,	action:'link',	url:'wAllowance-payrollcost', attr:'DEV' }
		],
	},{ //########################################################################################

		menuNo	: '7',
		menuName: '재무회계',
		item	:[
			{ name:'통장내역 조회/입력',	action:'popup',	url:'/PU.ez?PGID=w4c-bank.statement',width:'1200', attr:"new",	height:'900',	 },
			{ name:'-' },
			{ name:'결의서 조회/관리', access_set:false },
			//{ name:'통장내역 조회/입력',	action:'popup',	script:'javascript:ezcare_w4c("USR_ACM_050000")', depth:1 },
			{ name:'검토요청 답변 입력',	action:'popup',	script:'javascript:ezcare_w4c("USR_ACM_020000")', depth:1 },
			{ name:'결의서 조회 및 수정',	action:'popup',	script:'javascript:ezcare_w4c("USR_ACM_040000")', depth:1 },
			{ name:'회계장부 출력',	action:'popup',	script:'javascript:ezcare_w4c("USR_ACM_010000")', depth:1 },
			{ name:'-' },
			{ name:'예산/결산 보고', access_set:false  },
			{ name:'추경보고',	action:'popup',	script:'javascript:ezcare_w4c("USR_BGT_030000")', depth:1 },
			{ name:'예산보고',	action:'popup',	script:'javascript:ezcare_w4c("USR_BGT_010000")', depth:1 },
			{ name:'결산보고',	action:'popup',	script:'javascript:ezcare_w4c("USR_BGT_040000")', depth:1 },
			{ name:'-' },
			{ name:'이전 회계',	old:true, action:'popup',	url:'/ABook/main.html', script:'javascript:window.open("/ABook/main.html","","width=1010, height=650")', attr:'' }
			/*{ name:'-' },
			{ name:'인증서 재등록',	action:'popup',	script:'javascript:ezcare_w4c("USR_CUS_020000")' },*/
		],
	},{ //########################################################################################

		menuNo	: '8',
		menuName: '세무/사회보험',
		item	:[
			{ name:'세무' },
			{ name:'원천세 신고',	action:'popup',	script:'javascript:ezcare_w4c("USR_TAX_010000")', depth:1 },
			{ name:'퇴직금 계산 및 퇴직소득세 신고',	action:'popup',	script:'javascript:ezcare_w4c("USR_TAX_020000")', depth:1 },
			{ name:'근로소득원천징수부',	action:'popup',	script:'javascript:ezcare_w4c("USR_TAX_030000")', depth:1 },
			{ name:'-' },

			{ name:'사회보험 신고요청' },
			{ name:'종사자 취득·상실 현황',	action:'popup',	script:'javascript:ezcare_w4c("USR_INS_090000")', depth:1},

			{ name:'신고요청(취득·상실)',	action:'popup',	script:'javascript:ezcare_w4c("USR_INS_010000")', depth:1},
			{ name:'정정신고(취득·상실)',	action:'popup',	script:'javascript:ezcare_w4c("USR_ETC_030000")', depth:1},
			{ name:'휴·복직 신고',	action:'popup',	script:'javascript:ezcare_w4c("USR_ETC_010000")', depth:1},

			{ name:'보수총액',	action:'popup',	script:'javascript:ezcare_w4c("USR_INS_012000")', depth:1 },
			{ name:'기타신고',	action:'popup',	script:'javascript:ezcare_w4c("USR_INS_011000")', depth:1 },

			{ name:'-' },
			{ name:'연말정산' },
			{ name:'중도퇴직자 연말정산',	action:'popup',	script:'javascript:ezcare_w4c("USR_TAX_090000")', depth:1 },
			{ name:'연말정산 신고',	action:'popup',	script:'javascript:ezcare_w4c("USR_TAX_060000")', depth:1 }

			// { name:'신고자료 조회',	action:'popup',	script:'javascript:ezcare_w4c("USR_TAX_040000")', depth:1 },
		],
	},{ //########################################################################################


		menuNo	: '9',
		menuName: '기관관리',
		item	:[
			{ name:'스케쥴',	width:'1100',	height:'700',	action:'link',	url:'agency-schedule', attr:'' },
			{ name:'-' },
			{ name:'서식자료실',	width:'1100',	height:'700',	action:'link',	url:'docAsm-d100', attr:'' },
			{ name:'-' },

			{ name:'정보관리 및 설정',  	width:'700',	height:'560',	action:'dialog',	url:'setting-f01', attr:'' },
			{ name:'재가기관 정보',		width:'600',	height:'560',	action:'dialog',	url:'setting-f01#tab0', depth:'1', attr:'' },
			{ name:'사업자 정보',			width:'600',	height:'560',	action:'dialog',	url:'setting-f01#tab1', depth:'1', attr:'' },
			{ name:'직인(도장)',			width:'600',	height:'560',	action:'dialog',	url:'setting-f01#tab2', depth:'1', attr:'' },
			{ name:'결재라인',			width:'600',	height:'560',	action:'dialog',	url:'setting-f01#tab3', depth:'1', attr:'' },
			{ name:'본인부담금 계좌',		width:'600',	height:'560',	action:'dialog',	url:'setting-f01#tab4', depth:'1', attr:'' },
			{ name:'이지케어 담당자',		width:'600',	height:'560',	action:'dialog',	url:'setting-f01#tab5', depth:'1', attr:'' },
			{ name:'-' },
			{ name:'이지케어이용료',	action:'link',	url:'customer-ezc_bill_list' },
			{ name:'-' },
			{ name:'이지케어 사용자 관리',	width:'900',	height:'700',	action:'dialog',	url:'user-a100', attr:'' },
			{ name:'사용자 관리',			width:'800',	height:'700',	action:'dialog',	url:'user-a100#tab0', depth:'1', attr:''},
			{ name:'로그인기록',			width:'800',	height:'700',	action:'dialog',	url:'user-a100#tab1', depth:'1', attr:''},
			{ name:'-' },
			{ name:'내 정보관리/수정',	width:'600',	height:'480',	action:'dialog',	url:'user-myInfo', attr:'' },
			{ name:'-' },
			//{ name:'문자 보내기→ 번호직접 입력',	width:'1100',	height:'550',	action:'dialog',	url:'mobile-sendO' , attr:'DEV'},
			{ name:'문자 발신번호 관리',		width:'880',	height:'680',	action:'popup',		url:'/PU.ez?PGID=mobile-returnNumber' },
			
			{ name:'자동이체 신청서',	width:'1000',	height:'535',	action:'popup',	script:'javascript:open_request_dialog("자동이체", bill_chk, accountingState)' },
			{ name:'자료보관 신청',		width:'700',	height:'480',	action:'popup',	script:'javascript:open_request_dialog("자료보관", bill_chk, accountingState)' },
			{ name:'이용취소 신청',		width:'700',	height:'500',	action:'popup',	script:'javascript:open_request_dialog("이용취소", bill_chk, accountingState)' },
			{ name:'이용취소 신청2',		width:'700',	height:'600',	action:'popup',	script:'javascript:open_request_dialog("이용취소2", bill_chk, accountingState)', attr:'DEV' }
		],
	},{ //########################################################################################

		menuNo	: '10',
		menuName: '기관평가',
		item	:[
			{ name:'기관평가',    	width:'1400',	height:'900',	action:'link',	action:'link',	url:'guide-E100' },
			{ name:'평가서류 작성현황',	action:'link',	url:'guide-E100#tab0',  depth:1 }, 
			{ name:'서류함(평가서류 작성)',	action:'link',	url:'guide-E100#tab1', depth:1 },
			{ name:'의무교육 수료현황',	action:'link',	url:'guide-E100#tab2', depth:1 },
			{ name:'평가매뉴얼&자가진단',	action:'link',	url:'guide-E100#tab3', depth:1 },
			{ name:'-' },
			{ name:'운영 매뉴얼',   	width:'1400',	height:'900',	action:'link',	action:'link',	url:'guide-E200' },
			{ name:'업무 운영가이드',	action:'link',	url:'guide-E200#tab0',  depth:1 },
			{ name:'모니터링 매뉴얼',	action:'link',	url:'guide-E200#tab1', depth:1,},
			{ name:'지정갱신제',		action:'link',	url:'guide-E200#tab2', depth:1, attr:'NEW'},
			{ name:'주요법령 & 고시',	action:'link',	url:'guide-E200#tab3',  depth:1  },
			{ name:'노무자문',			action:'link',	url:'guide-E200#tab4',  depth:1  },

			{ name:'페이지 (파일)없음',	action:'DEV',	url:'nopage', attr:'DEV' },
			{ name:'페이지 접근권한 없음',	action:'DEV',	url:'denied', attr:'DEV' },
			{ name:'서명테스트',					width:'800',	height:'700',	action:'DEV',	url:'sign-write', attr:'DEV'},
			{ name:'아이콘_test',	width:'1100',	height:'700',	action:'link',	url:'patient-icon', attr:'DEV'},
			{ name:'POPUP-test',	width:'1100',	height:'700',	action:'popup',	url:'/PU.ez?PGID=patient-icon', attr:'DEV'},
			{ name:'파일올리기',	width:'1100',	height:'700',	action:'link',	url:'customer-file', attr:'DEV'}
		]
	}
]

if(typeof CHK_MASTER=='undefined') var CHK_MASTER = false;
if(typeof _dev_nav_badge=='undefined') var _dev_nav_badge = "";

function header_nav_set(){
	$.each(main_nav_item, function(idx, nav){
		var ul = $('<ul class="nav-menu-dropdown">'),
			no = nav.menuNo,	//상위번호(메인매뉴 번호)
			no_sub = 1;			//하위번호(드롭다운 하위순번)

		$.each(nav.item, function(key, item){
			var li = $("<li>"), a = $("<a class='nav-menu-dropdown-item'>"), url = item.url;

			if(item.url && _dev_nav_badge.match(item.url)) $(li).attr("ux",1);

			if(item.attr){
				if( !CHK_MASTER && item.attr.match(/DEV/) ) return;
				$.each($.trim(item.attr).split(" "), function(key, val){
					$(li).attr(val, 1);
				});
			}
	
			if(item.name=="-") return $(ul).append($(li).addClass("nav-menu-dropdown-divider"));

			if(item.depth) $(li).append('<em>└</em>').css("padding-left", "10px");
			// else if (item.attr && item.attr.match(/DEV/)) $(li).append('<em>'+(no+'.'+'dev</em>');
			else $(li).append('<em>'+(no+'.'+(no_sub++))+'</em>');
			// console.log(item.attr.match(/DEV/));

			$(a).append(item.name);

			if(!item.action || item.action=="disabled"){
				$(li).attr("disabled", true);

			}else if(item.action=="dialog"){
				url = "/PU.ez?page=dialog&PGID="+url;
				$(a).attr({
						"dialog-url": url,
						"dialog-title": item.name.replace(/<[^>]*>?/g, ''),
						"dialog-width": item.width || 600,
						"dialog-height": item.height || 600,
						"dialog-position": item.position || ""
				});
				$(li).attr("dialog", true);

			}else if(item.action=="script"){
				$(a).attr("href", item.url).addClass("popup-icon");
				$(li).attr("popup", true);

			}else if(item.action=="popup"){
				if(item.script){
					if(item.old) $(a).attr("href", item.script).addClass("old popup-icon");
					else $(a).attr("href", item.script).addClass("popup-icon");
				}else{
					$(a).attr("href", 'javascript:window.open("'+item.url+'","","width='+(item.width ? item.width : 1000)+', height='+(item.height ? item.height : 600)+'")').addClass("popup-icon");
				}
			}else{
				$(a).attr("href", "?PGID="+item.url );
				if(item.old) $(a).attr("href", "?PGID="+item.url+"&old=old" ).addClass("old");
			}

			$(li).append($(a));

			if(!item.old && (item.width || item.height)){
				url = "/PU.ez?page=popup&PGID="+item.url;
				if(item.action=="old") url = item.url;
				$(li).append(
					$('<a class="btn-win-popup">').attr({
						url: url,
						width: item.width || 1000,
						height: item.height || 700,
						name: no+"_"+key
					}).append('<svg class="icon popup" style="width:50px; margin-left:-10px;"><use xlink:href="#icon-arrow-up-right-square-fill"></use></svg>')
				);
			}
			/*
			if(item.youtube){
				$(li).append(
					$('<a class="btn-mov-help">').attr("youtube", item.youtube).append('<svg class="icon youtube" style="width:50px; margin-left:-10px;"><use xlink:href="#icon-video"></use></svg>')
				);
			}*/

			if(item.action=="dialog") $(li).append('<a><svg class="icon dialog"><use xlink:href="#icon-dialog"></use></svg></a>');
			else if(item.action=="popup") $(li).append('<a><svg class="icon popup"><use xlink:href="#icon-arrow-up-right-square-fill"></use></svg></a>');
			else $(li).append('<a><svg class="icon popup"></svg></a>');

			$(ul).append( $(li) );
		});
		$(".nav-menu-item[nav-no="+no+"]").prepend('<i class="no">'+no+'</i>');
		$(".nav-menu-item[nav-no="+no+"]").append($(ul));
	});

	$(".nav-menu-dropdown .btn-win-popup").click(function(){
		//if($(this).hasClass("youtube")) return;
		var url = $(this).attr("url");
		var winOpt = "width="+$(this).attr("width")+", height="+$(this).attr("height");
		window.open(url, "w"+$(this).attr("name"), winOpt );
	});

	$(".nav-menu-item a[href^='?PGID="+PGID+"']").closest("li.nav-menu-item").addClass("active");

	$("#nav-top .nav-menu-item").on({
		click: function(e) {
			$(this).addClass("hover").siblings().removeClass("hover");
			if($(this).parent().hasClass("dropdown-on"))
				$(this).parent().removeClass("dropdown-on");
			else if(!$(e.target).hasClass("direct-link"))
				$(this).parent().addClass("dropdown-on");

		}, mouseleave: function(){
			if(!$(this).parent().hasClass("dropdown-on")) $(this).removeClass("hover");

		}, mouseenter: function() {
			$(this).addClass("hover").siblings().removeClass("hover");
		}
	});
	$(window).mousedown(function(e){
		if(!$(e.target).closest(".nav-menu-item").length){
			$("#nav-top .nav-menu").removeClass("dropdown-on");
			$("#nav-top .nav-menu .nav-menu-item").removeClass("hover");
		}
	});
}