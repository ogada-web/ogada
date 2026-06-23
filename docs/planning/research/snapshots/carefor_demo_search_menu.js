var _____WB$wombat$assign$function_____=function(name){return (globalThis._wb_wombat && globalThis._wb_wombat.local_init && globalThis._wb_wombat.local_init(name))||globalThis[name];};if(!globalThis.__WB_pmw){globalThis.__WB_pmw=function(obj){this.__WB_source=obj;return this;}}{
let window = _____WB$wombat$assign$function_____("window");
let self = _____WB$wombat$assign$function_____("self");
let document = _____WB$wombat$assign$function_____("document");
let location = _____WB$wombat$assign$function_____("location");
let top = _____WB$wombat$assign$function_____("top");
let parent = _____WB$wombat$assign$function_____("parent");
let frames = _____WB$wombat$assign$function_____("frames");
let opener = _____WB$wombat$assign$function_____("opener");
var search_key = [];
var search_cnt = [];

/*
    2019.04.30 윤관석
    현황검색 / 그룹선택 / 등급선택 등을 이용하여 목록을 filter 한 후 목록상에서 ajax form submit 하였을 경우 처리 완료 후 해당 검색 조건 유지하기 위함
 */
var g_filter_values = {};

/*
    2019.07.15 윤관석
    setFilterValues(reset)
    page loading 후 검색조건 유지 처리
    (javascript 함수 구현전에는 검색조건 유지 필요한 페이지 마다 dom ready 후 선언했고 REQUEST 값에 filter_apply 가 있을 경우에만 처리했지만 전체 반영하는것으로 수정함)
 */
function setFilterValues(reset) {
  console.info('setFilterValues');
  if (reset) {
    console.info('setFilterValues : reseted');
    g_filter_values = {};
  }
  else {
    console.info('setFilterValues : apply filters');
    console.info(g_filter_values);
    for (var s in g_filter_values) {
      for (var btn_key in g_filter_values[s]) {
        console.info('... ' + s);
        var map_key = g_filter_values[s][btn_key]['map_key'];
        var obj_type = g_filter_values[s][btn_key]['obj_type'];

        console.log("map_key  : " + map_key);
        console.log("btn_key  : " + btn_key);
        console.log("obj_type : " + obj_type);

        if( obj_type == 'input')
        {
	      $(map_key).val(g_filter_values[s][btn_key]['value']).trigger("keyup");
        }
        else
        {
          if (map_key && $(map_key).length == 1 && g_filter_values[s][btn_key]['value']) {
            console.info('... values : ' + g_filter_values[s][btn_key]['value']);
            $("#" + btn_key).click();
          
            if (Array.isArray(g_filter_values[s][btn_key]['value'])) {
              console.info('apply filter len : ' + g_filter_values[s][btn_key]['value'].length);
              for (var v = 0; v < g_filter_values[s][btn_key]['value'].length; v++) {
                console.info('set : ' + g_filter_values[s][btn_key]['value'][v]);
                if (g_filter_values[s][btn_key]['value'].length == v + 1) {
                  console.info('click apply');
                  if ($(map_key).find("input[type=checkbox][searchbox][value='" + g_filter_values[s][btn_key]['value'][v] + "']").prop('checked') == false) {
                    $(map_key).find("input[type=checkbox][searchbox][value='" + g_filter_values[s][btn_key]['value'][v] + "']").click();
                  }
                }
                else {
                  console.info('prop checked apply')
                  $(map_key).find("input[type=checkbox][searchbox][value='" + g_filter_values[s][btn_key]['value'][v] + "']").prop('checked', true);
                }
              }
            }
            else {
              $(map_key).find("[obj-type='" + obj_type + "'][value='" + g_filter_values['value'][s] + "']").click();
            }
          
            $(map_key).hide();
          }
        }
      }
    }
  }
}

function close_final_filter() {
  $("#" + g_final_filter_id).hide();
}

$(document).on("click", "*[obj-type=openSearchMenu]", function(e) {
  var this_target = e.target;

  console.info('openSearchMenu filter open');

  try {
    var btn_pos = $(this_target).offset();
    var menu_info = $.parseJSON($(this_target).attr('menu-info').replace(/\'/g, "\""));
    console.info('filter menu info');
    console.info(menu_info);

    var menu_top = btn_pos.top + $(this_target).height();
    var menu_left = btn_pos.left;

    $("div[obj-type=searchmenu][id!='" + menu_info.id + "']").hide();
    $("#" + menu_info.id)
      .attr("btn_id", $(this_target).attr('id'))              // 화면상에 버튼
      .attr("btn_title", $(this_target).attr('title'))           // 버튼에 적용할 기본값
      .attr("list_table", menu_info.table_id)                     // 검색을 filter 할 table
      .attr("search_key", menu_info.key)                          // 검색을 적용할 key
      .attr("not_regist_global", menu_info.not_regist_global ? '1' : '0')  // 페이지 이동시 검색 유지 해제여부
      .css("position", "fixed")
      .css("top", menu_top)
      .css("left", menu_left)
      .css("z-index", 9999)
      .show()
      ;

    g_final_filter_id = menu_info.id;

    $(document.body).on('click', function(e) {
      if ($(e.target).closest("#" + menu_info.id).length === 0) {
        $("#" + menu_info.id).hide();
      }
    });
  }
  catch (e) {
    alert('서브메뉴 정보 분석에 실패했습니다. [' + e + ']');
  }
});

function searchTableWithButton(table_id, obj)
{
    var not_regist_global = $(obj).attr("not_regist_global") == '1' ? true : false;
    var key               = $(obj).attr("name");
    var id                = $(obj).attr("id");
    
    if (!not_regist_global) {
      if (!g_filter_values[key]) g_filter_values[key] = new Object();
      g_filter_values[key][id] = new Object();
      g_filter_values[key][id]['value'] = $(obj).val();
      g_filter_values[key][id]['map_key'] = "#" + id;
      g_filter_values[key][id]['obj_type'] = "input";
      console.log("lkajsdlkfjasl;kdfj");
    }
    
    if(search_key[table_id]['input'] === undefined) search_key[table_id]['input'] = [];
    search_key[table_id]['input'][key] = $(obj).val();
	table_search_field(table_id);
}

// 2020.06.08 윤관석, 검색 버튼 멀티선택으로 일괄 기능 고도화
$(document).on("change", "input[type='checkbox'][searchbox]", function(e) {

  console.info('filterApply event .. [' + $(this).val() + '] > checked? : ' + $(this).is(":checked"));

  var search_menu = $(this).closest("div[obj-type='searchmenu']");
  var btn_id = $(search_menu).attr("btn_id");
  var btn_title = $(search_menu).attr("btn_title");
  var table_id = $(search_menu).attr("list_table");
  var key = $(search_menu).attr("search_key");
  var not_regist_global = $(search_menu).attr("not_regist_global") == '1' ? true : false;
  var attr_key = $(this).attr('attr-key') ? $(this).attr('attr-key') : '';
  var map_key = search_menu.attr("id");
  var obj_type = $(e.target).next("[obj-type]").attr("obj-type");

  /*
  console.info("-----------------------console--------");
  console.info('filterApply > span searchbtn clicked > btn_id : ' + btn_id);
  console.info('filterApply > span searchbtn clicked > btn_title : ' + btn_title);
  console.info('filterApply > span searchbtn clicked > table_id : ' + table_id);
  console.info('filterApply > span searchbtn clicked > not_regist_global : ' + not_regist_global);
  console.info('filterApply > span searchbtn clicked > key : ' + key);
  console.info('filterApply > span searchbtn clicked > attr_key : ' + attr_key);
  console.info('filterApply > span searchbtn clicked > map_key : ' + map_key);
  console.info('filterApply > span searchbtn clicked > obj_type : ' + obj_type);
  */

  if ($(this).val() == '') {
    console.info('set no filters.. all btn checked..');

    // 전체를 선택할 경우 전체는 on /  나머지 모든 검색 값 off
    search_menu.find("input[type=checkbox][searchbox]").each(function() {
      $(this).prop('checked', $(this).val() == '' ? true : false);
    });
  }

  var check_values;
  var check_titles;

  if (attr_key) {
    // 한 검색 filter 안에 여러개의 검색 조건이 포함되어 있을 경우
    // (예. 생활실 검색 : 건물 / 층 / 생활실 검색이 같이 이루어짐)
    // 생활실 검색의 경우 포함관계가 있기 때문에 포함관계에 따른 자동 on/off 는 검색 레이어에서 구현했으며, 기본검색(생활실)이 아닌 다른검색(건물/층)은 이곳에서 이루어짐.
    // 이 경우 기본 key 가 아닌 검색 레이어에서 지정한 attr-key 를 검색 key로 사용
    console.info('use search key By attr-key : ' + attr_key);
    check_values = $(search_menu).find("input[type=checkbox][searchbox][attr-key='" + attr_key + "'][value!='']:checked").map(function() { return $(this).val(); }).get();
    check_titles = $(search_menu).find("input[type=checkbox][searchbox][attr-key='" + attr_key + "'][value!='']:checked").map(function() { return $(this).attr('text-value'); }).get();
    key = attr_key;
  }
  else {
    check_values = $(search_menu).find("input[type=checkbox][searchbox][value!='']:not([attr-key]):checked").map(function() { return $(this).val(); }).get();
    check_titles = $(search_menu).find("input[type=checkbox][searchbox][value!='']:not([attr-key]):checked").map(function() { return $(this).attr('text-value'); }).get();
  }

  // 선택된 검색 조건이 있을 경우 전체 off , 없을 경우 전체 on
  {
    var total_check_values = $(search_menu).find("input[type=checkbox][searchbox][value!='']:checked").map(function() { return $(this).val(); }).get();
    search_menu.find("input[type=checkbox][value='']").prop('checked', total_check_values.length == 0 ? true : false);
  }

  console.info('filterApply > span searchbtn clicked > val : ' + check_values);



  // 1. 검색버튼 제목 변경 및 global filter 반영
  if (check_values.length == 0) {
    console.info('values len = 0');
    $("#" + btn_id).text(btn_title);
    $("#" + btn_id).attr("now_val", "");

    if (!not_regist_global) {
      if (!g_filter_values[key]) g_filter_values[key] = new Object();
      g_filter_values[key][btn_id] = new Object();
      g_filter_values[key][btn_id]['value'] = '';
      g_filter_values[key][btn_id]['map_key'] = '';
      g_filter_values[key][btn_id]['obj_type'] = '';
    }
  }
  else {
    console.info('values len = ' + check_titles.length);
    $("#" + btn_id).text(check_titles.length == 1 ? check_titles[0] : check_titles[0] + "..."); // check_titles.join()
    $("#" + btn_id).attr("now_val", check_values.join());

    if (!not_regist_global) {
      if (!g_filter_values[key]) g_filter_values[key] = new Object();
      g_filter_values[key][btn_id] = new Object();
      g_filter_values[key][btn_id]['value'] = check_values;
      g_filter_values[key][btn_id]['map_key'] = "#" + map_key;
      g_filter_values[key][btn_id]['obj_type'] = obj_type;
    }
  }

  // 2. 서브 메뉴 Hide
  // $("div[obj-type=searchmenu]").hide();

  // 3. 검색 항목 추가
  search_key[table_id][key] = check_values;

  // 최초 검색이 생활실 검색의 경우 global 변수(건물/층) renew 필요
  //    if($(search_menu).attr("search_key") == 'ctrfkey')
  //    {
  //        search_key [ table_id ]['ctbfkey'] = g_filter_values['ctbfkey'] = $(search_menu).find("input[type=checkbox][searchbox][attr-key='ctbfkey'][value!='']:checked").map(function() { return $(this).val();} ).get();
  //        search_key [ table_id ]['ctbflor'] = g_filter_values['ctbflor'] = $(search_menu).find("input[type=checkbox][searchbox][attr-key='ctbflor'][value!='']:checked").map(function() { return $(this).val();} ).get();
  //
  //        console.info('ctbfkey : ' + search_key [ table_id ]['ctbfkey']);
  //        console.info('ctbflor : ' + search_key [ table_id ]['ctbflor']);
  //        console.info('ctrfkey : ' + search_key [ table_id ]['ctrfkey']);
  //    }



  // 4. 검색결과별 표시 처리
  table_search_field(table_id);

  // 5. 검색버튼 제목 change trigger
  $("#" + btn_id).trigger("change");
});






$(document).on("click", "li[obj-type='searchbtn']", function(e) {
  var this_target = e.target;

  //search
  var table_id = $(this).parent().attr("list-table");
  var key = $(this).parent().attr("search-key");
  var val = $(this).attr("value");
  var cbfunction = $(this).attr("cbfunction");

  //    console.log(table_id);
  //    console.log(key);
  //    console.log(val);

  // 1. 리스트 over 클래스 제거 후 선택한 리스트만 over 클래스 추가
  $("li[obj-type='searchbtn']").removeClass("over");
  $(this).addClass("over");

  // 2. 검색결과별 표시 처리
  $("#" + table_id).find("tbody tr").hide();
  if (!val) $("#" + table_id).find("tbody tr[data-number]").show();
  else $("#" + table_id).find("tbody tr[data-number=" + val + "]").show();

  var show_cnt = $("#" + table_id).find("tbody tr[data-number]:visible").size();
  if (show_cnt == 0) $("#" + table_id).find("tbody tr[none_search]").show();
  else $("#" + table_id).find("tbody tr[none_search]").hide();

  if (cbfunction) window[cbfunction]();
});


$(document).on("click", "span[obj-type='searchbtn_input']", function(e) {
  var this_target = e.target;

  //search name

  var table_id = $(this).attr("list-table");
  var target_id = $(this).attr("target-id");
  var val = $("#" + target_id).attr("value");

  // 유사 검색결과별 표시 처리
  $("#" + table_id).find("tbody tr").hide();
  if (!val) $("#" + table_id).find("tbody tr[data-name]").show();
  else $("#" + table_id).find("tbody tr[data-name*=" + val + "]").show();

});


function table_search_field(table_id)
{
    // $("#"+table_id).find("tbody tr").each(function(){ $(this).show();});

    search_cnt[table_id] = [];
    // console.info(table_id);

    let gridTableFlag = false;
    let gtFlag = false;
    let gtEl = document.getElementById(table_id);

    if(table_id != "plan_list_table")
    {
        var target_element = "tbody tr";

        // 2022.03.30 added by thPark grid table 추가
        if($("#" + table_id)[0].localName != "table")
        {
            if(gtEl.tagName == "G-T")
            {
                gtFlag = true;
                target_element = "g-tf";

                initGridTableAutoRowspan(gtEl);

                gtEl.querySelectorAll(setArrayToString([target_element], {prefix: ":scope > g-b > "})).forEach(item => item.dataset.filtering = false);
                [...gtEl.querySelectorAll(setArrayToString(gtElement, {prefix: ":scope > g-b > "}))].filter(el => el.dataset.filteringFlag != "false").forEach(item => item.classList.add("noneItem"));
            }
            else
            {
                gridTableFlag = true;
                target_element = "div[flag]";

                initAutoRowspan(gtEl);

                const flagChildren = getGridTableChildren(gtEl, "[flag]");
                for(const flagChild of flagChildren)
                {
                    for(const child of findSelector("[grid-row='" + flagChild.getAttribute("grid-row") + "']", gtEl))
                    {
                        child.setAttribute("filtering", "false");
                        if(!child.hasAttribute("flag")) child.style.display = "none";
                    }
                }
            }
        }
    }
    else if(table_id == "plan_list_table")
    {
        var target_element = "tbody tr span";
    }

    $("#" + table_id).find(target_element).each(function (idx) {
        var data = parse_comp_json($(this).attr('data-info'));

        if(data !== false)
        {
            //console.info('current search key of : ' + table_id);
            //console.info(search_key[table_id]);
            // 누적 검색결과에 모두 부합되는지 검사

            if(!gridTableFlag && !gtFlag)
            {
                if(table_id != "plan_list_table")
                {
                    $(this).hide();
                }
                else if(table_id == "plan_list_table")
                {
                    $(this).not('.no_hide').hide();
                }
            }

            for(var s_key in search_key[table_id])
            {
                if(s_key == "indexOf") continue;

                // 2019.08.23 ssk 수급자 리포트 페이지에서 기록지 (s_key == "report") key 조건 추가
                // 2020.04.10 윤관석 프로그램 수급자 그룹 조회 조건 추가
                if(s_key == "report" || s_key == "pgmname_key_str" || s_key == "program_group_key_text" || s_key == "phgname")
                {
                    console.log("here");
                    var temp_search_str = data[s_key];
                    var temp_search_arr = [];

                    if(temp_search_str !== '' && temp_search_str !== undefined && temp_search_str != null) temp_search_arr = temp_search_str.split(',');

                    var temp_flag = 0;

                    if(search_key[table_id][s_key] != '')
                    {
                        for(var temp_i = 0; temp_i < temp_search_arr.length; temp_i++)
                        {
                            if(Array.isArray(search_key[table_id][s_key]))
                            {
                                if(search_key[table_id][s_key].length && $.inArray(temp_search_arr[temp_i], search_key[table_id][s_key]) >= 0)
                                {
                                    temp_flag++;
                                }
                            }
                            else
                            {
                                if((search_key[table_id][s_key] && temp_search_arr[temp_i]) == search_key[table_id][s_key])
                                {
                                    temp_flag++;
                                }
                            }
                        }

                        if (temp_flag == 0) return;
                    }
                }
                else if(s_key == "pvctype")
                {

                    var pam_val = String(data[s_key]);
                    var tmp_arr = search_key[table_id][s_key];
                    var exists = false;

                    if(tmp_arr.length > 0)
                    {
                        if(pam_val == '') return;
                        var pam_arr = pam_val.split(',');

                        if('0생일테스트' == data['pamname'])
                        {
                            console.log(data);
                            console.log(data['pamname'] + " >>> " + pam_val + " >>> " + data['pvctype']);
                            console.log(tmp_arr);
                        }

                        for(var i = 0; i < pam_arr.length; i++)
                        {
                            if('0생일테스트' == data['pamname'])
                            {
                                console.log(pam_arr[i]);
                            }

                            if($.inArray(pam_arr[i], tmp_arr) >= 0)
                            {
                                exists = true;
                                break;
                            }
                            if('0생일테스트' == data['pamname'])
                            {
                                console.log(exists);
                            }
                        }
                        if(!exists) return;
                    }
                }
                else if(s_key == "pvctype_w_fam")
                {

                    var pam_val = String(data[s_key]);
                    var tmp_arr = search_key[table_id][s_key];
                    var exists = false;

                    if(tmp_arr.length > 0)
                    {
                        if(pam_val == '') return;
                        var pam_arr = pam_val.split(',');

                        for(var i = 0; i < pam_arr.length; i++)
                        {
                            if($.inArray(pam_arr[i], tmp_arr) >= 0)
                            {
                                exists = true;
                                break;
                            }
                        }
                        if(!exists) return;
                    }
                }
                // 2019.08.26 ssk input 검색어 조회 추가
                else if(s_key == "input")
                {
                    var temp_search_arr = search_key[table_id]['input'];
                    var temp_flag = 0;
                    for(var arr_key in temp_search_arr)
                    {
                        var tmp_str = String(data[arr_key]);
                        // if (temp_search_arr[arr_key] != '' && tmp_str.indexOf(temp_search_arr[arr_key]) >= 0) {
                        //     temp_flag++;
                        // }
                        // 2019.08.27 ssk 소이사님 의견 ( or 조건이였으나 and 조건으로 변경요청함 )
                        if(temp_search_arr[arr_key] != '' && tmp_str.indexOf(temp_search_arr[arr_key]) < 0) return;
                    }
                    // if(temp_flag == 0) return;
                }
                else if(s_key == "ctrfkey" || s_key == "ctbflor" || s_key == "ctbfkey")
                {
                    var checked_cnt = 0;
                    checked_cnt += Array.isArray(search_key[table_id]['ctrfkey']) ? search_key[table_id]['ctrfkey'].length : 0;
                    checked_cnt += Array.isArray(search_key[table_id]['ctbflor']) ? search_key[table_id]['ctbflor'].length : 0;
                    checked_cnt += Array.isArray(search_key[table_id]['ctbfkey']) ? search_key[table_id]['ctbfkey'].length : 0;

                    // 생활실 검색의 경우 세가지 검색(건물/층/생활실)조건이 OR로 동작해야함
                    if(checked_cnt)
                    {
                        if((Array.isArray(search_key[table_id]['ctrfkey']) && search_key[table_id]['ctrfkey'].length && $.inArray(String(data['ctrfkey']), search_key[table_id]['ctrfkey']) >= 0) || (Array.isArray(search_key[table_id]['ctbflor']) && search_key[table_id]['ctbflor'].length && $.inArray(data['ctbflor'] ? data['ctbflor'].replace(/(\S+)\s+_/g, '$1_').replace(/ +/g, (match) => "-".repeat(match.length)) : '', search_key[table_id]['ctbflor']) >= 0) || (Array.isArray(search_key[table_id]['ctbfkey']) && search_key[table_id]['ctbfkey'].length && $.inArray(String(data['ctbfkey']), search_key[table_id]['ctbfkey']) >= 0))
                        {
                        }
                        else
                        {
                            return;
                        }
                    }
                }
                else
                {
                    if(search_key[table_id][s_key])
                    {
                        if(Array.isArray(search_key[table_id][s_key]))
                        {
                            if(search_key[table_id][s_key].length && $.inArray(unescapeHtml(String(data[s_key])), search_key[table_id][s_key]) < 0) return;
                        }
                        else
                        {
                            if(data[s_key] != search_key[table_id][s_key]) return;
                        }
                    }
                }
            }

            // 검색결과 부합시 해당 값의 건수 반영
            for(var s_key in data)
            {
                var s_val = data[s_key];
                if(search_cnt[table_id][s_key] === undefined) search_cnt[table_id][s_key] = [];
                if(search_cnt[table_id][s_key][s_val] === undefined) search_cnt[table_id][s_key][s_val] = 0;
                search_cnt[table_id][s_key][s_val]++;
            }

            if(!gridTableFlag && !gtFlag) $(this).show();
            else
            {
                if(gridTableFlag)
                {
                    for(const child of findSelector("[grid-row='" + this.getAttribute("grid-row") + "']", gtEl))
                    {
                        child.setAttribute("filtering", "true");
                        if(!child.hasAttribute("flag")) child.style.display = "flex";
                    }
                }
                else if(gtFlag)
                {
                    this.dataset.filtering = true;
                    getGridTableSameRowItems(this).forEach(item => item.classList.remove("noneItem"));
                }
            }
        }
    });

    if(gridTableFlag)
    {
        setGridTablesBorder(gtEl);
        setAutoRowspan(gtEl, false);
        setScrollBottomBorder(gtEl);
        setSelectedRow(table_id);
        toggleNone(gtEl);
    }
    else if(gtFlag) initGridTable(gtEl);

    // 5. 조회된 값 없을 경우 처리
    let show_cnt = 0;

    if(gridTableFlag)
    {
        show_cnt = getGridTableChildren(getGridTableById(table_id), "[flag][filtering='true']").length;
    }
    else if(gtFlag)
    {
        show_cnt = $(`#${table_id} g-t g-b g-tf[data-filtering="true"]`).length;
    }
    else
    {
        show_cnt = $("#" + table_id).find("tbody tr[data-info]:visible").size();
        if(show_cnt == 0)
        {
            $("#" + table_id).find("tbody tr[none_search]").show();
        }
        else
        {
            $("#" + table_id).find("tbody tr[none_search]").hide();

            // 2017.02.03 added by thPark 기존 선택되었던 tr이 조회조건에 맞지 않을 땐, 맨 상단의 tr 클릭
            var _selected_flag = false;
            $("#" + table_id + " tbody tr:visible").each(function (index) {
                $(this).find("td[data-field=index]").text(index + 1);
                if($(this).hasClass("spot_color"))
                {
                    // console.info('by spot_color _selected_flag true');
                    _selected_flag = true;
                }

                // 2019.05.02 윤관석 : 첫번재 td 에 img checkbox 있을 경우 첫번째 라인 자동 선택하지 않도록 수정
                if($(this).find("td").eq(0).find("img[data-rel='check_img']").length)
                {
                    // console.info('by check_img _selected_flag true');
                    _selected_flag = true;
                }

                // 2019.05.02 윤관석 : 첫번재 td 에 input type checkbox 있을 경우 첫번째 라인 자동 선택하지 않도록 수정
                if($(this).find("td").eq(0).find("input[type='checkbox']").length)
                {
                    // console.info('by checkbox _selected_flag true');
                    _selected_flag = true;
                }

                // 2019.07.15 added by thPark 디폴트 체크 없애는 속성 추가
                if($(this).find("td").eq(0).find("img").attr("default-check") == "false")
                {
                    // console.info('by img default-check == false _selected_flag true');
                    _selected_flag = true;
                }

                if($(this).find("td").eq(0).attr("default-check") == "false")
                {
                    // console.info('by default-check == false _selected_flag true');
                    _selected_flag = true;
                }
            });

            if(!_selected_flag)
            {
                // console.info('first list auto select.');
                // 2020.06.09 윤관석, cursor = pointer 일 경우에만 클릭하도록 수정, 문제 발생시 나에게 알려주기 바람, 억지스럽게 적용..
                if($("#" + table_id + " tbody tr:visible").eq(0).find("td").eq(0).css('cursor') == 'pointer')
                {
                    $("#" + table_id + " tbody tr:visible").eq(0).click();
                }
            }
        }
    }

    // 6. 조회건수 표시
    setSearchListTotalCount(table_id, show_cnt);

    // 7. 합계 표시 부분. [사용방법 : 재가급여 '5-1. 본인부담금 청구관리' 참조]
    setSearchListTotalSum(table_id);

    // CF-4123 작성건수/대상자수 세팅
    setSearchListStatus(table_id);
}


var ___pre_table_id = '';
var ___pre_table_data = [];

function resetSearchTableList() {
  ___pre_table_id = '';
  ___pre_table_data = [];
}

function searchTableList(table_id, searchForm, container_id)
{
    // 2022.03.10 added by thPark searchForm ID 지정
    var searchFormID = searchForm == undefined ? "searchItem" : searchForm;

    console.log('in searchTableList : ' + container_id);

    var search_data = {};
    // 2019.08.27 ssk 검색조건 초기화
    if(!container_id) g_filter_values = {};
    search_key[table_id] = [];
    // 2019.08.27 ssk
    var search_date_length = 0;

    //console.log('in searchTableList .. ');

    $("#" + searchFormID + " * ").serializeArray().map(function (x) {
        // 2019.08.27 ssk input 검색어를 search_key[ table_id ]에 추가

        //console.log('in serializeArray map .. ');

        if(search_key[table_id]['input'] === undefined) search_key[table_id]['input'] = [];

        if(x.value != '')
        {

            //console.log('in serializeArray map .. value : ' + x.value);

            search_data[x.name] = x.value;
            search_key[table_id]['input'][x.name] = x.value === undefined ? '' : x.value;
            search_date_length++;

        }
        else search_key[table_id]['input'][x.name] = '';
    });

    //console.info('search_data:');
    //console.info('table_id:'+table_id);
    //console.info(search_data);
    //search_key[table_id] = [];
    //table_search_field(table_id);

    //if(___pre_table_id != table_id)
    {
        var obj_menu = !container_id ? $("*[obj-type=openSearchMenu]") : $("#" + container_id + " *[obj-type=openSearchMenu]");

        obj_menu.each(function () {
            var ot = $("#" + $(this).attr("id")).text();
            var tt = $(this).attr("title");
            if(ot != tt)
            {
                $("#" + $(this).attr("id")).text($(this).attr("title"));
                $("#" + $(this).attr("id")).trigger("change");
            }
        });
    }
    var ___searched = false;
    var total_show_cnt = 0; // 2019.08.27 ssk 검색 총 건수
    search_cnt[table_id] = []; // 검색 건수 Object


    // 2022.03.31 added by thPark grid table 대응
    let gridTableFlag = false;
    let gtFlag = false;
    let gtEl = document.getElementById(table_id);

    var target_element = "tbody tr";
    if(table_id == "plan_list_table") target_element = "tbody tr span";

    if($("#" + table_id)[0].localName != "table")
    {
        if(gtEl.tagName == "G-T")
        {
            gtFlag = true;
            target_element = "g-tf";

            initGridTableAutoRowspan(gtEl);

            gtEl.querySelectorAll(setArrayToString([target_element], {prefix: ":scope > g-b > "})).forEach(item => item.dataset.filtering = false);
            [...gtEl.querySelectorAll(setArrayToString(gtElement, {prefix: ":scope > g-b > "}))].filter(el => el.dataset.filteringFlag != "false").forEach(item => item.classList.add("noneItem"));
        }
        else
        {
            gridTableFlag = true;
            target_element = "div[flag]";

            initAutoRowspan(gtEl);

            const flagChildren = getGridTableChildren(gtEl, "[flag]");
            for(const flagChild of flagChildren)
            {
                for(const child of findSelector("[grid-row='" + flagChild.getAttribute("grid-row") + "']", gtEl))
                {
                    child.setAttribute("filtering", "false");
                    if(!child.hasAttribute("flag")) child.style.display = "none";
                }
            }
        }
    }

    $("#" + table_id).find(target_element + "[data-info]").each(function (idx) {

        var row_data = false;

        if(___pre_table_id != table_id)
        {
            row_data = ___pre_table_data[idx] = parse_comp_json($(this).attr('data-info'));
        }
        else
        {
            row_data = ___pre_table_data[idx];
            // console.info('1');
        }
        //var row_data = parse_comp_json($(this).attr('data-info'));
        //var row_data = false;

        if(row_data !== false)
        {
            // console.log(row_data.pamname + " - " + search_data.pamname + " : " + row_data.pamname.indexOf(search_data.pamname));
            var show_cnt = 0;
            for(var key in search_data)
            {
                //console.info( typeof row_data[key] );
                // if(typeof row_data[key] == 'string')
                {
                    ___searched = true;
                    // if(row_data[key].indexOf(search_data[key]) >= 0) show_cnt++;
                    // 2019.08.27 ssk 소이사님 의견 ( or 조건이였으나 and 조건으로 변경요청함 )
                    // if(search_data[key] != '' && row_data[key].indexOf(search_data[key]) < 0)
                    const regex = new RegExp(search_data[key], 'i');
                    if(search_data[key] != '' && String(row_data[key]).search(regex) < 0)
                    {
                        show_cnt = 0;
                        break;
                    }

                    show_cnt++;
                }
            }

            if(show_cnt > 0 || search_date_length == 0)
            {

                // 2019.08.27 ssk 검색결과 부합시 해당 값의 건수 반영
                for(var s_key in row_data)
                {
                    var s_val = row_data[s_key];
                    if(search_cnt[table_id][s_key] === undefined) search_cnt[table_id][s_key] = [];
                    if(search_cnt[table_id][s_key][s_val] === undefined) search_cnt[table_id][s_key][s_val] = 0;
                    search_cnt[table_id][s_key][s_val]++;
                }
                total_show_cnt++;

                if(!gridTableFlag && !gtFlag) $(this).show();
                else
                {
                    if(gridTableFlag)
                    {
                        for(const child of findSelector("[grid-row='" + this.getAttribute("grid-row") + "']", gtEl))
                        {
                            child.setAttribute("filtering", "true");
                            if(!child.hasAttribute("flag")) child.style.display = "flex";
                        }
                    }
                    else if(gtFlag)
                    {
                        this.dataset.filtering = true;
                        getGridTableSameRowItems(this).forEach(item => item.classList.remove("noneItem"));
                    }
                }
            }
            else
            {
                if(!gridTableFlag && !gtFlag) $(this).hide();
            }
        }
    });

    if(gridTableFlag)
    {
        setGridTablesBorder(gtEl);
        setAutoRowspan(gtEl, false);
        setScrollBottomBorder(gtEl);
        setSelectedRow(table_id);
        toggleNone(gtEl);
    }
    else if(gtFlag) initGridTable(gtEl);

    // if($("#"+table_id+" tbody tr:visible").length == 0) $("#"+table_id+" tbody tr[data-info]").show();
    if(___searched == false) $("#" + table_id + " tbody tr[data-info]").show();

    // 2019.08.27 ssk 조회된 값 없을 경우 처리
    let visible_cnt = 0;

    if(gridTableFlag) visible_cnt = getGridTableChildren(getGridTableById(table_id), "[flag][filtering='true']").length;
    else if(gtFlag) visible_cnt = $(`#${table_id} g-t g-b g-tf[data-filtering="true"]`).length;
    else visible_cnt = $("#" + table_id).find("tbody tr[data-info]:visible").size();

    if(visible_cnt == 0)
    {
        $("#" + table_id).find("tbody tr[none_search]").show();
    }
    else
    {
        $("#" + table_id).find("tbody tr[none_search]").hide();
    }

    // 2019.08.27 ssk 건수 셋팅
    setSearchListTotalCount(table_id, total_show_cnt);
    // 2019.09.03 ssk 합계 셋팅
    // 7. 합계 표시 부분. [사용방법 : 재가급여 '5-1. 본인부담금 청구관리' 참조]
    setSearchListTotalSum(table_id);

    // CF-4123 작성건수/대상자수 세팅
    setSearchListStatus(table_id);

    ___pre_table_id = table_id;

    // 2022.03.10 added by thPark call back function
    if($("#" + table_id).attr("cbfunc"))
    {
        var cbfunc = $.parseJSON($("#" + table_id).attr("cbfunc").replace(/\'/gi, '"'));

        executeFunction(cbfunc.func, window, cbfunc.param);
    }
}

function searchTableList2(table_id, obj) {
  var this_input = $(obj);
  var this_form = this_input.closest("form");
  var search_data = {};
  this_form.serializeArray().map(function(x) { if (x.value != '') search_data[x.name] = x.value; });

  $("*[obj-type=openSearchMenu]").each(function() {
    var ot = $("#" + $(this).attr("id")).text();
    var tt = $(this).attr("title");
    if (ot != tt) {
      $("#" + $(this).attr("id")).text($(this).attr("title"));
      $("#" + $(this).attr("id")).trigger("change");
    }
  });

  var ___searched = false;
  $("#" + table_id + " tbody tr").each(function(idx) {

    var row_data = false;

    if (___pre_table_id != table_id) {
      row_data = ___pre_table_data[idx] = parse_comp_json($(this).attr('data-info'));
    }
    else {
      row_data = ___pre_table_data[idx];
      // console.info('1');
    }

    if (row_data !== false) {
      var search_cnt = 0;
      for (var key in search_data) {
        if (typeof row_data[key] == 'string') {
          ___searched = true;
          if (row_data[key].indexOf(search_data[key]) >= 0) search_cnt++;
        }
      }

      if (search_cnt > 0) $(this).show();
      else $(this).hide();
    }

  });

  if (___searched == false) $("#" + table_id + " tbody tr[data-info]").show();

  ___pre_table_id = table_id;
}

// 윤관석 (2018.03.06)
// form 구분하여 검색 : : /work/layer/modal/nursing/mod.commission_doctor_record.php 참조 (3-1.간호급여제공 > 7.진료기록 > 계약의사진료 일괄처리)
function searchTableListByFormId(form_id, table_id)
{
    var search_data = {};
    $("#" + form_id).serializeArray().map(function (x) {
        if(x.value != '') search_data[x.name] = x.value;
    });

    search_key[table_id] = [];

    table_search_field(table_id);

    $("*[obj-type=openSearchMenu]").each(function () {
        $("#" + $(this).attr("id")).text($(this).attr("title"));
        $("#" + $(this).attr("id")).trigger("change");
    });

    $("#" + table_id + " tbody tr:visible").each(function () {
        var row_data = parse_comp_json($(this).attr('data-info'));

        if(row_data !== false && row_data != '')
        {
            //console.log(row_data.pamname + " - " + search_data.pamname + " : " + row_data.pamname.indexOf(search_data.pamname));
            var search_cnt = 0;
            for(var key in search_data) if(row_data[key].indexOf(search_data[key]) >= 0) search_cnt++;

            if(search_cnt > 0) $(this).show(); else $(this).hide();
        }
    });

    if($("#" + table_id + " tbody tr:visible").length == 0) $("#" + table_id + " tbody tr[data-info]").show();

    $("#" + table_id + " tbody tr[data-info]:visible").each(function(index) { $(this).find("td[data-field=index]").text(index + 1); });
}

// 2019.09.04 tab별 검색할 경우 form 이 여러개 존재하여 form id로 구분
function searchTableListByTab(form_id, table_id) {
  console.log(form_id);
  console.log(table_id);
  var search_data = {};
  // 2019.08.27 ssk 검색조건 초기화
  g_filter_values = {};
  search_key[table_id] = [];
  // 2019.08.27 ssk
  var search_date_length = 0;

  // 2024.11.12 은나현 :: div에서도 개별 검색 되게 하기 위한 * 추가
  $("#" + form_id + " * ").serializeArray().map(function(x) {
    // 2019.08.27 ssk input 검색어를 search_key[ table_id ]에 추가
    if (search_key[table_id]['input'] === undefined) search_key[table_id]['input'] = [];

    if (x.value != '') {

      search_data[x.name] = x.value;
      search_key[table_id]['input'][x.name] = x.value === undefined ? '' : x.value;
      search_date_length++;

    } else search_key[table_id]['input'][x.name] = '';
  });
  //search_key[table_id] = [];
  //table_search_field(table_id);

  //if(___pre_table_id != table_id)
  {
    $("*[obj-type=openSearchMenu]").each(function() {
      var ot = $("#" + $(this).attr("id")).text();
      var tt = $(this).attr("title");
      if (ot != tt) {
        $("#" + $(this).attr("id")).text($(this).attr("title"));
        $("#" + $(this).attr("id")).trigger("change");
      }
    });
  }

  searchTableListResult(table_id, search_data, search_date_length);
}

// 2019.09.04 input 검색함수를 나누게 되어 검색하는 부분만 따로 분리
function searchTableListResult(id, data, length)
{

    var table_id = id;
    var search_data = data;
    var search_date_length = length;
    var ___searched = false;
    var total_show_cnt = 0; // 2019.08.27 ssk 검색 총 건수
    search_cnt[table_id] = []; // 검색 건수 Object
    $("#" + table_id + " tbody tr[data-info]").each(function (idx) {

        var row_data = false;

        if(___pre_table_id != table_id)
        {
            row_data = ___pre_table_data[idx] = parse_comp_json($(this).attr('data-info'));
            // console.log("first");
        }
        else
        {
            row_data = ___pre_table_data[idx];
            // console.info('1');
        }
        //var row_data = parse_comp_json($(this).attr('data-info'));
        //var row_data = false;

        if(row_data !== false)
        {
            var show_cnt = 0;
            for(var key in search_data)
            {
                // console.info( typeof row_data[key] );
                if(typeof row_data[key] == 'string')
                {
                    ___searched = true;
                    // if(row_data[key].indexOf(search_data[key]) >= 0) show_cnt++;
                    // 2019.08.27 ssk 소이사님 의견 ( or 조건이였으나 and 조건으로 변경요청함 )
                    if(search_data[key] != '' && row_data[key].indexOf(search_data[key]) < 0)
                    {
                        show_cnt = 0;
                        break;
                    }

                    show_cnt++;
                }
            }

            if(show_cnt > 0 || search_date_length == 0)
            {

                // 2019.08.27 ssk 검색결과 부합시 해당 값의 건수 반영
                for(var s_key in row_data)
                {
                    var s_val = row_data[s_key];
                    if(search_cnt[table_id][s_key] === undefined) search_cnt[table_id][s_key] = [];
                    if(search_cnt[table_id][s_key][s_val] === undefined) search_cnt[table_id][s_key][s_val] = 0;
                    search_cnt[table_id][s_key][s_val]++;
                }
                total_show_cnt++;

                $(this).show();
            }
            else $(this).hide();
        }

    });

    // if($("#"+table_id+" tbody tr:visible").length == 0) $("#"+table_id+" tbody tr[data-info]").show();
    if(___searched == false) $("#" + table_id + " tbody tr[data-info]").show();

    // 2019.08.27 ssk 조회된 값 없을 경우 처리
    var visible_cnt = $("#" + table_id).find("tbody tr[data-info]:visible").size();
    if(visible_cnt == 0)
    {
        $("#" + table_id).find("tbody tr[none_search]").show();
    }
    else
    {
        $("#" + table_id).find("tbody tr[none_search]").hide();
    }

    // 2019.08.27 ssk 건수 셋팅
    setSearchListTotalCount(table_id, total_show_cnt);
    // 2019.09.03 ssk 합계 셋팅
    // 7. 합계 표시 부분. [사용방법 : 재가급여 '5-1. 본인부담금 청구관리' 참조]
    setSearchListTotalSum(table_id);

    // CF-4123 작성건수/대상자수 세팅
    setSearchListStatus(table_id);

    ___pre_table_id = table_id;
}

// 6. 조회건수 표시
function setSearchListTotalCount(id, cnt) {
    var table_id = id;
    var show_cnt = cnt;
    let gridTableFlag = false;
    let gtFlag = false;

    if($("#" + table_id)[0].localName != "table")
    {
        if($("#" + table_id)[0] == "G-T") gtFlag = true;
        else gridTableFlag = true;
    }

    $("span[data-type=seachedCount][data-rel=" + table_id + "][data-key=all").text(show_cnt);
    $("span[data-type=seachedCount][data-rel=" + table_id + "][data-key!=all]").each(function() {

        var fieldnam = $(this).attr("data-key");
        var fieldval = $(this).attr("data-val");

        if (search_cnt[table_id][fieldnam] !== undefined && search_cnt[table_id][fieldnam][fieldval] !== undefined) {
            $(this).text(search_cnt[table_id][fieldnam][fieldval]);
        }
        else {
            $(this).text(0);
        }
    });


    //2019.11.12 Added By Kimmw, 연번정보 확인
    if(gridTableFlag)
    {
        for([index, flagChild] of getGridTableChildren(getGridTableById(table_id), "[flag][filtering='true']").entries())
        {
            let indexTarget = nextUntil(flagChild, "[flag]", defaultGridTarget).filter( el => el.matches("[data-field='index']") )[0];
            if(indexTarget) indexTarget.innerText = (index + 1).toString();
        }
    }
    else if(gtFlag){}
    else
    {
        // $("#" + table_id + " tbody tr:visible").each(function(index) { $(this).find("td[data-field=index]").text(index + 1); });
        $("#" + table_id + " tbody td[data-field=index]:visible").each(function(index) { $(this).text(index + 1); });
    }
}
// 7. 합계 표시 부분. [사용방법 : 재가급여 '5-1. 본인부담금 청구관리' 참조]
function setSearchListTotalSum(id)
{
    var table_id = id;

    $("span[data-type=seachedSum][data-rel=" + table_id + "]").each(function () {

        var fieldnam = $(this).attr("data-key");
        var num_sum = 0;
        // console.info( table_id + ":" + fieldnam );
        $("#" + table_id + " td[data-key='" + fieldnam + "']:visible, #" + table_id + " div[data-key='" + fieldnam + "']:visible, #" + table_id + " g-td[data-key='" + fieldnam + "']:visible").each(function () {
            num_sum += parseInt($(this).attr('data-val') ? $(this).attr('data-val') : "0", 10);
        });
        // console.info( "NUM_SUM : " + num_sum );
        $(this).text(number_format(num_sum));

    });
}

// 작성건수 / 대상자수. [사용방법 : 주야간 '3-2.상태변화 기록' 참조]
function setSearchListStatus(id)
{
    var table_id = id;

    $("span[data-type=searchedStatus][data-rel=" + table_id + "]").each(function(){

        // CF-4455 작성/미작성 외 id로 분자/분모 계산 추가 [사용방법 : 시설 8-10.연간관리현황 > 근골격계질환검사 조치/증상 참조]
        if($(this).attr('numerator') !== undefined && $(this).attr('denominator') !== undefined)
        {
            var numerator_cnt = 0;
            var denominator_cnt = 0;
            var numerator = $(this).attr('numerator');
            var denominator = $(this).attr('denominator');

            $("#" + table_id).find("span[filter-for=" + numerator + "]:visible").each(function(){
                if($(this).hasClass('info_sbox_on')) numerator_cnt++;
            });

            $("#" + table_id).find("span[filter-for=" + denominator + "]:visible").each(function(){
                if($(this).hasClass('info_sbox_on')) denominator_cnt++;
            });

            $(this).html(numerator_cnt.toString() + ' / ' + denominator_cnt.toString());
        }
        else
        {
            var grid_column = this.closest('g-th').dataset.gtCol;
            var target_cnt = 0;
            var record_cnt = 0;
            var error_cnt = 0;

            $("#" + table_id).find("g-td[data-gt-col=" + grid_column + "]").each(function(){
                const gtfEl = getGridTableDataFlag(this);

                if(gtfEl.dataset.filtering != 'false')
                {
                    if($(this).hasClass('complete') && !$(this).is('[data-no-count]'))
                    {
                        target_cnt++;
                        record_cnt++;
                    }
                    else if($(this).hasClass('none') || $(this).hasClass('none_without_color'))
                    {
                        target_cnt++;
                    }

                    // CF-3855
                    if( $(this).find("*[data-type='error']").length > 0 )
                    {
                        error_cnt++;
                    }
                }
            });

            //$(this).text(record_cnt.toString() + ' / ' + target_cnt.toString());
            $(this).html(record_cnt.toString() + ( error_cnt ? "<span class='stxt' style='color:red'>("+error_cnt.toString()+")</span>":"" ) + ' / ' + target_cnt.toString());
        }
    });
}
}

/*
     FILE ARCHIVED ON 23:16:30 Jun 09, 2026 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 06:37:11 Jun 15, 2026.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  captures_list: 0.554
  exclusion.robots: 0.043
  exclusion.robots.policy: 0.032
  esindex: 0.009
  cdx.remote: 6.526
  LoadShardBlock: 135.749 (3)
  PetaboxLoader3.datanode: 91.882 (4)
  PetaboxLoader3.resolve: 108.494 (2)
  load_resource: 103.37
*/