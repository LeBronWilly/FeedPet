// js/hotel.js

ts(".ts.embed").embed();

// favorite hotel list table sort
ts('#my_fav_hotel_table').tablesort();

$("#chose_district").change(function () {
  var value = $("#chose_district").val();
  changeMap(value);
});

var hotel_nameDisplay = document.getElementById("hotel_name");
var rankDisplay = document.getElementById("rank");
var addressDisplay = document.getElementById("address");
var phoneDisplay = document.getElementById("phone");
var inchargeDisplay = document.getElementById("incharge");

mapboxgl.accessToken =
  "pk.eyJ1Ijoic3Vubnl1bnVuIiwiYSI6ImNrNGxjd2FjMzBqYTYzbG41em1wZHhtYWwifQ.pRC4vs_4Oc-sATwbFuxbkg";
var map = new mapboxgl.Map({
  container: "map",
  style: "mapbox://styles/mapbox/streets-v11",
  center: [121.5, 25.025759],
  zoom: 11
});

function changeMap(district) {
  $.ajax({
    url: "/hotel/map/" + district,
    type: "GET",
    dataType: "json",
    success: function (data) {
      if (data) {
        // console.log("changeMap");
        // console.log(data);
        var geo_add = data;

        var map = new mapboxgl.Map({
          container: "map",
          style: "mapbox://styles/mapbox/streets-v11",
          center: [121.5, 25.025759],
          zoom: 11
        });

        function pointvalue(geo_add) {
          console.log(geo_add);
          return geo_add;
        }

        map.on("load", function () {
          // console.log("onload");
          // console.log(typeof geo_add);

          map.addSource("national-park", {
            type: "geojson",
            data: geo_add,
            // generateId: true
          });

          function animateMarker() {
            console.log("animatemaker");
            map.getSource("national-park").setData({
              type: "geojson",
              data: pointvalue(geo_add)
            });
          }
          map.addLayer({
            id: "park-volcanoes",
            type: "circle",
            source: "national-park",
            paint: {
              "circle-radius": 7,
              "circle-color": "#B42222"
            },
            filter: ["==", "$type", "Point"]
          });
          var quakeID = null;

          map.on('mouseenter', 'park-volcanoes', (e) => {
            var hotel_name = e.features[0].properties.full_name;
            var rank = e.features[0].properties.rank;
            var hotel_id = e.features[0].id;
            console.log(hotel_id)

            // Check whether features exist
            if (e.features.length > 0) {
              // Display the magnitude, location, and time in the sidebar
              hotel_nameDisplay.textContent = hotel_name;
              rankDisplay.textContent = rank;

              // If quakeID for the hovered feature is not null,
              // use removeFeatureState to reset to the default behavior
              if (quakeID) {
                map.removeFeatureState({
                  source: "national-park",
                  id: quakeID
                });
              }
              $('#show_detail').attr("onclick", "location.href='/hotel/hotel_detail/" + hotel_id + "'")
              //點心條
              ts('.snackbar').snackbar({
                content: '你選中了：' + hotel_name
              });

              quakeID = e.features[0].id;
              console.log(quakeID)


              map.setFeatureState({
                source: 'national-park',
                id: quakeID,
              }, {
                hover: true
              });
            }
          });
        });
      }
    },
    error: function (err) { }
  });
}

// 增加hotel favorite
function add_hotel_favor(master_id, hotel_id) {
  var result
  $.ajax({
    url: '/hotel/add_hotel_favor/' + master_id + '/' + hotel_id,
    type: 'GET',
    dataType: 'json',
    async: false, //啟用同步請求
    success: function (data) {
      console.log(data)
      result = data
    },
    error: function (err) {
    }
  });
  return result
}

// 刪除hotel favorite
function del_hotel_favor(master_id, hotel_id) {
  var result
  $.ajax({
    url: '/hotel/del_hotel_favor/' + master_id + '/' + hotel_id,
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

// [hotel_detail]增加hotel favorite
function add_hotel_favor_detail(master_id, hotel_id) {
  var result = add_hotel_favor(master_id, hotel_id)
  if (result) {
    if (result.status == true) {
      //點心條
      ts('.snackbar').snackbar({
        content: '成功加入我的最愛'
      });
      $('#detail_fav_btn_' + hotel_id).removeClass("positive").addClass("negative")
      $('#detail_fav_btn_' + hotel_id).html('<i class="heart icon"></i>移除最愛')
      $('#detail_fav_btn_' + hotel_id).attr("onclick", "del_hotel_favor_detail(" + master_id + ", " + hotel_id + ")")
    }
    else {
      //點心條
      ts('.snackbar').snackbar({
        content: '已經加過了'
      });
    }
  }
}

// [hotel_detail]刪除hotel favorite
function del_hotel_favor_detail(master_id, hotel_id) {
  var result = del_hotel_favor(master_id, hotel_id)
  if (result) {
    if (result.status == true) {
      //點心條
      ts('.snackbar').snackbar({
        content: '成功移除我的最愛'
      });
      $('#detail_fav_btn_' + hotel_id).removeClass("negative").addClass("positive")
      $('#detail_fav_btn_' + hotel_id).html('<i class="heart icon"></i>加入最愛')
      $('#detail_fav_btn_' + hotel_id).attr("onclick", "add_hotel_favor_detail(" + master_id + ", " + hotel_id + ")")
    }
    else {
      //點心條
      ts('.snackbar').snackbar({
        content: '無法移除'
      });
    }
  }
}

// [my_favorite_hotel]刪除hotel favorite
function del_my_favor_hotel(master_id, hotel_id) {
  var result = del_hotel_favor(master_id, hotel_id)
  if (result) {
    if (result.status == true) {
      //點心條
      ts('.snackbar').snackbar({
        content: '成功移除我的最愛'
      });
      window.location.href = '/hotel/my_favor_hotel';
    }
    else {
      //點心條
      ts('.snackbar').snackbar({
        content: '無法移除'
      });
    }
  }
}
