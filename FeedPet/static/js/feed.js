// feed tab
ts('#first.tabbed.menu .item').tab({
    onSwitch: (tabName, groupName) => {
        // alert("你切換到了「" + tabName + "」分頁，而群組是「" + groupName + "」。");
    }
});

// feed list table sort
ts('.ts.sortable.table').tablesort();

//使用者透過下拉式選單選擇狗狗
$("#choseDog").change(function () {
    $("#choseDog option:selected").each(function () {
        var value = $("#choseDog").val();
        getDogInfo(value)
    });
});

//使用者透過下拉式選單選擇貓貓
$("#choseCat").change(function () {
    $("#choseCat option:selected").each(function () {
        var value = $("#choseCat").val();
        getCatInfo(value)
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
    console.log(petinfo);
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

                //點心條
                ts('.snackbar').snackbar({
                    content: '計算結果如右邊欄位'
                });
            }
        },
        error: function (err) {
            console.log("nononon")
        }
    });
});

//將貓貓資訊透過ajax送到後端計算完再傳回來
$("#cat_cal").click(function () {
    var weight = $("#cat_weight").val();
    var type = $("#cat_type").val();
    var ligation = $(".cat_ligation:checked").val();
    var cal_petclass = 'dog'
    var petinfo = { 'weight': weight, 'type': type, 'ligation': ligation, 'cal_petclass': cal_petclass };
    console.log(petinfo);
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
                    content: '計算結果如右邊欄位'
                });
            }
        },
        error: function (err) {
            console.log("nononon")
        }
    });
});

// feed list 動態搜尋
function searchFeedTable() {
    var input, filter, table, tr, td, i;
    input = document.getElementById("search_input");
    filter = input.value.toUpperCase();
    table = document.getElementById("feed_table");
    tr = table.getElementsByTagName("tr");

    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

// 增加feed favorite
function add_feed_favor(master_id, feed_id) {
    $.ajax({
        url: '/feed/add_feed_favor/' + master_id + '/' + feed_id,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            if (data) {
                //點心條
                ts('.snackbar').snackbar({
                    content: '成功加入我的最愛'
                });
            }
        },
        error: function (err) {
        }
    });
}

// 刪除feed favorite
function del_feed_favor() {

}
