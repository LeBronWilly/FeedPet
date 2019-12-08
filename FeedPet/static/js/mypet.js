// mypet del button
ts('.dismissable.message').message();
function showDimmer_delpet() {
    ts('#closableModal_delpet').modal("show")
}

// mypet 彈跳提示訊息
ts('[data-tooltip]').popup();

// mypet add pet chose petType
const dogSubType = ["成犬(室內/中低活動量)", "成犬(中高度活動量)", "需增重成犬(輸入目標體重)", "需減肥成犬(輸入目標體重)", "成長期幼犬(斷奶至4個月)", "成長期幼犬(4個月至10個月)", "懷孕母犬(前42天)", "懷孕母犬(最後21天)", "哺乳母犬"];
const catSubType = ["成貓(室內/低活動量)", "成貓(中高活動量)", "需增重成貓(輸入目標體重)", "需減肥成貓(輸入目標體重)", "成長期幼貓(10個月以內)", "老貓(11歲以上)", "懷孕母貓", "哺乳母貓"];
Array.prototype.forEach.call(document.forms.addpet.petClass, radio => {
    radio.addEventListener('change', () => {

        //先將原先petType下的元素清空
        var div = document.getElementById("petType");
        while (div.hasChildNodes()) {
            div.removeChild(div.firstChild);
        }
        if (document.getElementById("cat").checked) {
            for (j = 0; j < catSubType.length; j++) {
                var option = document.createElement('option');
                option.innerHTML = catSubType[j];
                document.getElementById("petType").appendChild(option);
            }
            //console.log(`${document.forms.addpet.petClass.value}`);
        }
        //判斷選取到dog時候
        if (document.getElementById("dog").checked) {
            for (i = 0; i < dogSubType.length; i++) {
                var option = document.createElement('option');
                option.innerHTML = dogSubType[i];
                document.getElementById("petType").appendChild(option);
            }
            //console.log(`${document.forms.addpet.petClass.value}`);
        }
    })
});

// mypet preview image(add/update)
$("#imgInp").change(function () {
    //當檔案改變後，做一些事 
    readURL(this);   // this代表<input id="imgInp">
});
function readURL(input) {
    if (input.files && input.files[0]) {
        var imageTagID = input.getAttribute("targetID");
        var reader = new FileReader();
        reader.onload = function (e) {
            var img = document.getElementById(imageTagID);
            img.setAttribute("src", e.target.result)
        }
        reader.readAsDataURL(input.files[0]);
    }
}

window.onload = getTime();
//取得系统当前时间
function getTime() {
    console.log(tMonth)
    var today = new Date();
    var tYear = today.getFullYear();
    var tMonth = today.getMonth() + 1;
    var tDate = today.getDate();
    document.getElementById("showDate").innerHTML = tYear + "-" + tMonth + "-" + tDate;
}
