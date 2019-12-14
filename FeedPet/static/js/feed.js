// feed tab
ts('#first.tabbed.menu .item').tab({
    onSwitch: (tabName, groupName) => {
        //點心條
        ts('.snackbar').snackbar({
            content: '你切換到 [ ' + tabName + ' ] 的分頁了'
        });
    }
});

// feed list table sort
// ts('.ts.sortable.table').tablesort();

//使用者透過下拉式選單選擇狗狗
$("#choseDog").change(function () {
    $("#choseDog option:selected").each(function () {
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
});

//使用者透過下拉式選單選擇貓貓
$("#choseCat").change(function () {
    $("#choseCat option:selected").each(function () {
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

// feed list 動態搜尋
// function searchFeedTable() {
//     var input, filter, table, tr, td, i;
//     input = document.getElementById("search_input");
//     filter = input.value.toUpperCase();
//     table = document.getElementById("feed_table");
//     tr = table.getElementsByTagName("tr"); 

//     for (i = 0; i < tr.length - 1; i++) {
//         td = tr[i].getElementsByTagName("td")[0];
//         if (td) {
//             if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
//                 tr[i].style.display = "";
//             } else {
//                 tr[i].style.display = "none";
//             }
//         }
//     }
// }

$("#feed_table").DataTable();

// 增加feed favorite
function add_feed_favor(master_id, feed_id) {
    $.ajax({
        url: '/feed/add_feed_favor/' + master_id + '/' + feed_id,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            if (data) {
                if (data.status == true) {
                    //點心條
                    ts('.snackbar').snackbar({
                        content: '成功加入我的最愛'
                    });
                }
                else {
                    //點心條
                    ts('.snackbar').snackbar({
                        content: '已經加過了'
                    });
                }
            }
        },
        error: function (err) {
        }
    });
}

// 刪除feed favorite
function del_feed_favor() {

}

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
