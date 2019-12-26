// js/hotel.js

ts(".ts.embed").embed();

$("#chose_district").change(function() {
  var value = $("#chose_district").val();
  changeMap(value);
});

function changeMap(district) {
  $.ajax({
    url: "/hotel/map/" + district,
    type: "GET",
    dataType: "json",
    success: function(data) {
      if (data) {
        console.log("changeMap");
        console.log(data);
        console.log("======");
        var geo_add = data;

        var map = new mapboxgl.Map({
          container: "map",
          style: "mapbox://styles/mapbox/streets-v11",
          center: [121.5, 25.025759],
          zoom: 10
        });

        function pointvalue(geo_add) {
          console.log(geo_add);
          return geo_add;
        }

        map.on("load", function() {
          console.log("onload");
          console.log(typeof geo_add);
          map.addSource("national-park", {
            type: "geojson",
            data: geo_add
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
              "circle-radius": 6,
              "circle-color": "#B42222"
            },
            filter: ["==", "$type", "Point"]
          });
        });
      }
    },
    error: function(err) {}
  });
}

mapboxgl.accessToken =
  "pk.eyJ1Ijoic3Vubnl1bnVuIiwiYSI6ImNrNGxjd2FjMzBqYTYzbG41em1wZHhtYWwifQ.pRC4vs_4Oc-sATwbFuxbkg";
var map = new mapboxgl.Map({
  container: "map",
  style: "mapbox://styles/mapbox/streets-v11",
  center: [121.5, 25.025759],
  zoom: 10
});

// function pointvalue(geo_add) {
//   console.log(geo_add);
//   return geo_add;
// }

// map.on("load", function() {
//   map.addSource("national-park", {
//     type: "geojson",
//     data: pointvalue({
//       type: "Point",
//       coordinates: [121.5, 25.025759]
//     })
//   });

//   function animateMarker() {
//     console.log("animatemaker");
//     map.getSource("national-park").setData({
//       type: "geojson",
//       data: pointvalue(geo_add)
//     });
//   }

//   // map.addLayer({
//   //   id: "park-boundary",
//   //   type: "fill",
//   //   source: "national-park",
//   //   paint: {
//   //     "fill-color": "#888888",
//   //     "fill-opacity": 0.4
//   //   },
//   //   filter: ["==", "$type", "Polygon"]
//   // });

//   map.addLayer({
//     id: "park-volcanoes",
//     type: "circle",
//     source: "national-park",
//     paint: {
//       "circle-radius": 6,
//       "circle-color": "#B42222"
//     },
//     filter: ["==", "$type", "Point"]
//   });

//   // map.on("mouseenter", "places", function() {
//   //   map.getCanvas().style.cursor = "pointer";
//   // });

//   map.on("click", "places", function(e) {
//     var coordinates = e.features[0].geometry.coordinates.slice();
//     var description = e.features[0].properties.description;

//     // Ensure that if the map is zoomed out such that multiple
//     // copies of the feature are visible, the popup appears
//     // over the copy being pointed to.
//     while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
//       coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
//     }

//     new mapboxgl.Popup()
//       .setLngLat(coordinates)
//       .setHTML(description)
//       .addTo(map);
//   });
// });
