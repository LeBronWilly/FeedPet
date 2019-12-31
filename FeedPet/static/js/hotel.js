// js/hotel.js

ts(".ts.embed").embed();

$("#chose_district").change(function () {
  var value = $("#chose_district").val();
  changeMap(value);
});

var hotel_nameDisplay = document.getElementById("hotel_name");
var rankDisplay = document.getElementById("rank");

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
        console.log("changeMap");
        console.log(data);
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
          console.log("onload");
          console.log(typeof geo_add);

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
          map.on('mousemove', function (e) {
            var features = map.queryRenderedFeatures(e.point, { layers: ['park-volcanoes'] });
            map.getCanvas().style.cursor = (features.length) ? 'pointer' : '';
          });
          map.on('click', function (e) {
            var features = map.queryRenderedFeatures(e.point, { layers: ['park-volcanoes'] });

            if (!features.length) {
              return;
            }

            var feature = features[0];

            var popup = new mapboxgl.Popup()
              .setLngLat(feature.geometry.coordinates)
              .setHTML("<button>加入我的最愛</button>")
              .addTo(map);
          });
        });
      }
    },
    error: function (err) { }
  });
}
