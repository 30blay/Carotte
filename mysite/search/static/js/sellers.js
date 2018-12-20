var dataurl = "../../data.geojson";

window.addEventListener("map:init", function (event) {
            var map = event.detail.map;

            fetch(dataurl)
              .then(function(resp) {
                return resp.json();
              })
              .then(function(data) {
                L.geoJson(data, {
                  onEachFeature: function onEachFeature(feature, layer) {
                      var marker = L.marker(feature.geometry.coordinates).addTo(map);
                }}).addTo(map);
              });
          });