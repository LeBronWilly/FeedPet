// js/hotel.js

ts(".ts.embed").embed();

$("#chose_district").change(function () {
  var value = $("#chose_district").val();
  changeMap(value);
});

// $("#show_detail").change(function () {
//   var value = $("#show_detail").val();
//   changedetail(value);
// });


// function changedetail(district) {
//   $.ajax({
//     url: "/hotel/hotel_detail/" + hotelid,
//     type: "GET",
//     dataType: "json",
//     success: function (data) {
//       if (data) {
//         var detail = data
//       }
//     },
//     error: function (err) { }
//   });
// }

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

          map.addSource("national-park", {
            type: "geojson",
            data: geo_add,
            generateId: true
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
            var address = e.features[0].properties.address;
            var phone = e.features[0].properties.phone;
            var incharge = e.features[0].properties.incharge;
            var hotel_id = e.features[0].id;

            // Check whether features exist
            if (e.features.length > 0) {
              // Display the magnitude, location, and time in the sidebar
              hotel_nameDisplay.textContent = hotel_name;
              rankDisplay.textContent = rank;
              addressDisplay.textContent = address;
              phoneDisplay.textContent = phone;
              inchargeDisplay.textContent = incharge;

              // If quakeID for the hovered feature is not null,
              // use removeFeatureState to reset to the default behavior
              if (quakeID) {
                map.removeFeatureState({
                  source: "national-park",
                  id: quakeID
                });
              }
              $('#show_detail').attr("onclick", "location.href='/hotel/hotel_detail/" + hotel_id + "'")

              quakeID = e.features[0].id;

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
