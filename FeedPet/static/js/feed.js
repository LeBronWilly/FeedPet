// js/feed.js

// feed list table sort
ts('#my_fav_feed_table').tablesort();

// feed tab
ts('#first.tabbed.menu .item').tab({
    onSwitch: (tabName, groupName) => {
        //點心條
        ts('.snackbar').snackbar({
            content: '你切換到 [ ' + tabName + ' ] 的分頁了'
        });
    }
});

//使用者透過下拉式選單選擇狗狗
$("#choseDog").change(function () {
    var value = $("#choseDog").val();
    getDogInfo(value)

    $("#setting").removeClass("active")
    $("#calculate").addClass("active")
    $("#favorite").removeClass("active")

    //點心條
    ts('.snackbar').snackbar({
        content: "以填入 [ " + $("#choseDog option:selected").text() + " ] 的資料"
    });
});

//使用者透過下拉式選單選擇貓貓
$("#choseCat").change(function () {
    var value = $("#choseCat").val();
    getCatInfo(value)

    $("#setting").removeClass("active")
    $("#calculate").addClass("active")
    $("#favorite").removeClass("active")

    //點心條
    ts('.snackbar').snackbar({
        content: "以填入 [ " + $("#choseCat option:selected").text() + " ] 的資料"
    });
});

//選擇了其中之一狗狗後，用ajax去後端抓狗狗資料，並套入現有欄位中
function getDogInfo(petId) {
    $.ajax({
        url: '/feed/getPet/' + petId,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            if (data) {
                $('#dog_weight').val(data.weight)
                $('#dog_type option').each(function (index, value) {
                    if ($(this).text() == data.petType) { // EDITED THIS LINE
                        $(this).prop('selected', true)
                    }
                });
                if (data.ligation == 'Yes') {
                    $('#dog_yes').prop('checked', true)
                } else {
                    $('#dog_no').prop('checked', true)
                }
            }
        },
        error: function (err) {
        }
    });
}

//選擇了其中之一貓貓後，用ajax去後端抓貓貓資料，並套入現有欄位中
function getCatInfo(petId) {
    $.ajax({
        url: '/feed/getPet/' + petId,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            if (data) {
                $('#cat_weight').val(data.weight)
                $('#cat_type option').each(function (index, value) {
                    if ($(this).text() == data.petType) { // EDITED THIS LINE
                        $(this).prop('selected', true)
                    }
                });
                if (data.ligation == 'Yes') {
                    $('#cat_yes').prop('checked', true)
                } else {
                    $('#cat_no').prop('checked', true)
                }
            }
        },
        error: function (err) {
        }
    });
}

//將狗狗資訊透過ajax送到後端計算完再傳回來
$("#dog_cal").click(function () {
    var weight = $("#dog_weight").val();
    var type = $("#dog_type").val();
    var ligation = $(".dog_ligation:checked").val();
    var cal_petclass = 'dog'
    var petinfo = { 'weight': weight, 'type': type, 'ligation': ligation, 'cal_petclass': cal_petclass };
    if (weight == null || type == null || ligation == null) {
        //點心條
        ts('.snackbar').snackbar({
            content: '請輸狗狗物資訊'
        });
    }
    else {
        $.ajax({
            url: '/feed/feed_calculation/',
            type: 'GET',
            data: petinfo,
            dataType: 'json',
            success: function (data) {
                if (data) {
                    console.log(data)
                    $('#dogcannedFood').val(data.cannedFood)
                    $('#dograwFood').val(data.rawFood)
                    $('#dogLyophilizerdRawFood').val(data.LyophilizerdRawFood)
                    $('#dogwater').val(data.water)

                    $("#setting").removeClass("active")
                    $("#calculate").removeClass("active")
                    $("#favorite").addClass("active")

                    //點心條
                    ts('.snackbar').snackbar({
                        content: '推薦餵食量如右邊欄位'
                    });
                }
            },
            error: function (err) {
                console.log("nononon")
            }
        });
    }
});

//將貓貓資訊透過ajax送到後端計算完再傳回來
$("#cat_cal").click(function () {
    var weight = $("#cat_weight").val();
    var type = $("#cat_type").val();
    var ligation = $(".cat_ligation:checked").val();
    var cal_petclass = 'dog'
    var petinfo = { 'weight': weight, 'type': type, 'ligation': ligation, 'cal_petclass': cal_petclass };
    if (weight == null || type == null || ligation == null) {
        //點心條
        ts('.snackbar').snackbar({
            content: '請輸入貓貓資訊'
        });
    }
    else {
        $.ajax({
            url: '/feed/feed_calculation/',
            type: 'GET',
            data: petinfo,
            dataType: 'json',
            success: function (data) {
                if (data) {
                    console.log(data)
                    $('#catcannedFood').val(data.cannedFood)
                    $('#catrawFood').val(data.rawFood)
                    $('#catLyophilizerdRawFood').val(data.LyophilizerdRawFood)
                    $('#catwater').val(data.water)

                    //點心條
                    ts('.snackbar').snackbar({
                        content: '推薦餵食量如右邊欄位'
                    });
                }
            },
            error: function (err) {
                console.log("nononon")
            }
        });
    }
});

//推薦狗狗飼料（假假）檢查欄位是否有空
function reco_dog_feed() {
    var weight = $("#dog_weight").val();
    var type = $("#dog_type").val();
    var ligation = $(".dog_ligation:checked").val();
    var dogcannedFood = $("#dogcannedFood").val();
    var dograwFood = $("#dograwFood").val();
    var dogLyophilizerdRawFood = $("#dogLyophilizerdRawFood").val();
    var dogwater = $("#dogwater").val();

    if (weight == null || type == null || ligation == null) {
        //點心條
        ts('.snackbar').snackbar({
            content: '請先輸入狗狗資訊'
        });
    }
    else if (dogcannedFood == null || dogcannedFood == "" ||
        dograwFood == null || dograwFood == "" ||
        dogLyophilizerdRawFood == null || dogLyophilizerdRawFood == "" ||
        dogwater == null || dogwater == "") {
        //點心條
        ts('.snackbar').snackbar({
            content: '請先計算狗狗餵食量'
        });
    }
    else {
        location.href = '/feed/feed_recommendation'
    }
}

// data table server side
$("#feed_table").DataTable({
    "lengthMenu": [10, 25, 50, 75, 100],
    "processing": true,
    "serverSide": true,
    "oLanguage": {
        "sProcessing": "處理中...",
        "sLengthMenu": "顯示 _MENU_ 筆記錄",
        "sZeroRecords": "無符合資料",
        "sInfo": "目前資料：_START_ - _END_ 總筆數：_TOTAL_",
        "sInfoEmpty": "無任何資料", "sInfoFiltered": "(過濾總筆數 _MAX_)",
        "sInfoPostFix": "",
        "sSearch": "搜尋",
        "sEmptyTable": "表格空空",
        "sLoadingRecords": "載入中...",
        "sUrl": "",
        "oPaginate": {
            "sFirst": "首頁",
            "sPrevious": "上一頁",
            "sNext": "下一頁",
            "sLast": "最後一頁"
        },
    },
    "ajax": {
        "url": "/api/feedList/",
        "type": "GET"
    },
    "columns": [
        {
            "data": null,
            "render": function (data, type, row, meta) {
                if (data["master_feed"] == 1) {
                    return '<button class="ts circular icon secondary button" id="list_fav_btn_' + data['id'] + '" onclick="del_feed_favor_list(' + user + ', ' + data['id'] + ')"><i class="negative heart icon" id="list_fav_i_' + data['id'] + '"></i></button>'
                }
                else {
                    return '<button class="ts circular icon secondary button" id="list_fav_btn_' + data['id'] + '" onclick="add_feed_favor_list(' + user + ', ' + data['id'] + ')"><i class="empty heart icon" id="list_fav_i_' + data['id'] + '"></i></button>'
                }
            }
        },
        { "data": "id" },
        { "data": "fname" },
        { "data": "fitem" },
        { "data": "fusage1" },
        { "data": "flegalname" },
        {
            "data": null,
            "render": function (data, type, row, meta) {
                return '<a href="/feed/feed_list/feed_detail/' + data['id'] + '">more</a>'
            }
        },
    ]
})

$('div.dataTables_length select').removeClass().addClass("ts basic dropdown");
$('#feed_table_filter').addClass("ts input");

// 增加feed favorite
function add_feed_favor(master_id, feed_id) {
    var result
    $.ajax({
        url: '/feed/add_feed_favor/' + master_id + '/' + feed_id,
        type: 'GET',
        dataType: 'json',
        async: false, //啟用同步請求
        success: function (data) {
            result = data
        },
        error: function (err) {
        }
    });
    return result
}

// 刪除feed favorite
function del_feed_favor(master_id, feed_id) {
    var result
    $.ajax({
        url: '/feed/del_feed_favor/' + master_id + '/' + feed_id,
        type: 'GET',
        dataType: 'json',
        async: false, //啟用同步請求
        success: function (data) {
            result = data
        },
        error: function (err) {
        }
    });
    return result
}

// [feed_recommendation]增加feed favorite
function add_feed_favor_reco(master_id, feed_id) {
    var result = add_feed_favor(master_id, feed_id)
    if (result) {
        if (result.status == true) {
            //點心條
            ts('.snackbar').snackbar({
                content: '成功加入我的最愛'
            });
            $('#reco_fav_i_' + feed_id).removeClass("empty").addClass("negative")
            $('#reco_fav_btn_' + feed_id).attr("onclick", "del_feed_favor_reco(" + master_id + ", " + feed_id + ")")
        }
        else {
            //點心條
            ts('.snackbar').snackbar({
                content: '已經加過了'
            });
        }
    }
}

// [feed_recommendation]刪除feed favorite
function del_feed_favor_reco(master_id, feed_id) {
    var result = del_feed_favor(master_id, feed_id)
    if (result) {
        if (result.status == true) {
            //點心條
            ts('.snackbar').snackbar({
                content: '成功移除我的最愛'
            });
            $('#reco_fav_i_' + feed_id).removeClass("negative").addClass("empty")
            $('#reco_fav_btn_' + feed_id).attr("onclick", "add_feed_favor_reco(" + master_id + ", " + feed_id + ")")
        }
        else {
            //點心條
            ts('.snackbar').snackbar({
                content: '無法移除'
            });
        }
    }
}

// [feed_list]增加feed favorite
function add_feed_favor_list(master_id, feed_id) {
    var result = add_feed_favor(master_id, feed_id)
    if (result) {
        if (result.status == true) {
            //點心條
            ts('.snackbar').snackbar({
                content: '成功加入我的最愛'
            });
            $('#list_fav_i_' + feed_id).removeClass("empty").addClass("negative")
            $('#list_fav_btn_' + feed_id).attr("onclick", "del_feed_favor_list(" + master_id + ", " + feed_id + ")")
        }
        else {
            //點心條
            ts('.snackbar').snackbar({
                content: '已經加過了'
            });
        }
    }
}

// [feed_list]刪除feed favorite
function del_feed_favor_list(master_id, feed_id) {
    var result = del_feed_favor(master_id, feed_id)
    if (result) {
        if (result.status == true) {
            //點心條
            ts('.snackbar').snackbar({
                content: '成功移除我的最愛'
            });
            $('#list_fav_i_' + feed_id).removeClass("negative").addClass("empty")
            $('#list_fav_btn_' + feed_id).attr("onclick", "add_feed_favor_list(" + master_id + ", " + feed_id + ")")
        }
        else {
            //點心條
            ts('.snackbar').snackbar({
                content: '無法移除'
            });
        }
    }
}

// [feed_detail]增加feed favorite
function add_feed_favor_detail(master_id, feed_id) {
    var result = add_feed_favor(master_id, feed_id)
    if (result) {
        if (result.status == true) {
            //點心條
            ts('.snackbar').snackbar({
                content: '成功加入我的最愛'
            });
            $('#detail_fav_btn_' + feed_id).removeClass("positive").addClass("negative")
            $('#detail_fav_btn_' + feed_id).html('<i class="heart icon"></i>移除最愛')
            $('#detail_fav_btn_' + feed_id).attr("onclick", "del_feed_favor_detail(" + master_id + ", " + feed_id + ")")
        }
        else {
            //點心條
            ts('.snackbar').snackbar({
                content: '已經加過了'
            });
        }
    }
}

// [feed_detail]刪除feed favorite
function del_feed_favor_detail(master_id, feed_id) {
    var result = del_feed_favor(master_id, feed_id)
    if (result) {
        if (result.status == true) {
            //點心條
            ts('.snackbar').snackbar({
                content: '成功移除我的最愛'
            });
            $('#detail_fav_btn_' + feed_id).removeClass("negative").addClass("positive")
            $('#detail_fav_btn_' + feed_id).html('<i class="heart icon"></i>加入最愛')
            $('#detail_fav_btn_' + feed_id).attr("onclick", "add_feed_favor_detail(" + master_id + ", " + feed_id + ")")
        }
        else {
            //點心條
            ts('.snackbar').snackbar({
                content: '無法移除'
            });
        }
    }
}

// [my_favorite_feed]刪除feed favorite
function del_my_favor(master_id, feed_id) {
    var result = del_feed_favor(master_id, feed_id)
    if (result) {
        if (result.status == true) {
            //點心條
            ts('.snackbar').snackbar({
                content: '成功移除我的最愛'
            });
            window.location.href = '/feed/my_favor_feed';
        }
        else {
            //點心條
            ts('.snackbar').snackbar({
                content: '無法移除'
            });
        }
    }
}
