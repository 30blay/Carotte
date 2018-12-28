        function populateMap(data){
            for(i in data) {
                var title = data[i].name,
                    loc = data[i].loc,
                    seller = data[i].seller,
                    marker = new L.Marker(new L.latLng(loc), {title: title} );
                map.addLayer(marker);
            }
        }

window.addEventListener("map:init", function(event){
        var map = event.detail.map;

        // use context variable instead of making AJAX call
        var map_products =  JSON.parse('{{ map_products }}');
        populateMap(map_products);
});

