// js/index.js

// 當網頁載入完畢關閉讀取指示器條
$(document).ready(function () {
    // $('#loading').hide()
});

// index user tag
ts('.ts.dropdown:not(.basic)').dropdown();

// index logout
ts('.dismissable.message').message();
function showDimmer_logout() {
    ts('#closableModal_logout').modal("show")
}

// close message
ts('.dismissable.message').message()
