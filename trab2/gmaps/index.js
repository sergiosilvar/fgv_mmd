// Enable the visual refresh
google.maps.visualRefresh = true;

// Rio de Janeiro
var rjLatLng = new google.maps.LatLng(-22.930338, -43.422649);
var map;
var heatmap;
var map_data;
var markersArray = [];
var kml_layer;
var ljson;


function initialize() {
    var mapOptions = {
      // Rio de Janerio.
      center: rjLatLng,
      zoom: 11,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    
    map = new google.maps.Map(document.getElementById("map-canvas"),
        mapOptions);



}
google.maps.event.addDomListener(window, 'load', initialize);







// Deletes all markers in the array by removing references to them
function delete_overlays() {
    if(heatmap){
        heatmap.setMap(null);
        heatmap = null
    }
    if (map_data) {
        for (i in map_data) {
            if(map_data[i].setMap)
                map_data[i].setMap(null);
        }
        map_data.length = 0;
    }
    if (kml_layer){
        kml_layer.setMap(null)
        kml_layer = null
    }
}
            
function load_map(results,type){
    delete_overlays()
    lines = CSVToArray(results)
    //alert('lines.lenght: '+lines.length)
    map_data = new Array();
    for(i=0; i<lines.length-1; i++){
        words = lines[i];
        if(words.length){
            lat = words[0];
            lng = words[1];
            price_m2= words[2];
            id_home=words[3];
            
            if (type=='heatmap_aglom'){
                point = new google.maps.LatLng(lat, lng);
            }
            
            if (type=='heatmap_rsm2'){
                // http://stackoverflow.com/questions/11296510/google-maps-api-v-3-heatmap-creation-issue
                point = {location: new google.maps.LatLng(lat, lng), weight: +price_m2}
            }
            
            if(type=='marker'){
                point = new google.maps.Marker({
                position: new google.maps.LatLng(lat, lng),
                map: map
                });
            
            }
            map_data.push(point);
            
        }
    }
    
    
    var my_gradient = [
        'rgba(0, 255, 255, 0)',
        'rgba(0, 255, 255, 1)',
        'rgba(0, 191, 255, 1)',
        'rgba(0, 127, 255, 1)',
        'rgba(0, 63, 255, 1)',
        'rgba(0, 0, 255, 1)',
        'rgba(0, 0, 223, 1)',
        'rgba(0, 0, 191, 1)',
        'rgba(0, 0, 159, 1)',
        'rgba(0, 0, 127, 1)',
        'rgba(63, 0, 91, 1)',
        'rgba(127, 0, 63, 1)',
        'rgba(191, 0, 31, 1)',
        'rgba(255, 0, 0, 1)'
     ]
    
    //http://www.perbang.dk/rgbgradient/
    var my_gradient2 = [
        'rgba(0,255,255,0)',
        'rgba(0,46,163,1)',
        'rgba(37,40,128,1)',
        'rgba(73,35,94,1)',
        'rgba(111,29,60,1)',
        'rgba(149,24,26,1)'
    ]
    if (type.indexOf('heatmap')>=0){
        heatmap = new google.maps.visualization.HeatmapLayer({
          data: map_data,
          gradient: my_gradient,
          dissipating: true,
          radius:60
        });
        heatmap.setMap(map);
    }
    
    if (type=='markers'){
    }
}

function load_limits(limits,type){
    if (type=='json'){
        if (limits){
            for (var i = 0; i < limits.features.length; i++) {
                //console.debug('limits')
            
                var item = limits.features[i];
                var coords = item.geometry.coordinates;
                /*
                var latLng = new google.maps.LatLng(coords[1],coords[0]);
                var marker = new google.maps.Marker({
                position: latLng,
                map: map
                });
                */
                // Construct the polygon
                bairro = new google.maps.Polygon({
                    paths: coords,
                    strokeColor: '#FF0000',
                    strokeOpacity: 0.8,
                    strokeWeight: 2,
                    fillColor: '#FF0000',
                    fillOpacity: 0.35
                });   
                bairro.setMap(map);
            }            
            
        }
    
    }
}

function load_kml(){
        kml_layer = new google.maps.KmlLayer('rj.kml');
        kml_layer.setMap(map);

}

function draw_map(type){
    console.info('Drawing '+type+'...')
   $(document).load('get_homes/csv', function(resp, status, xhr){
        if (status == 'success'){
            
            load_map(resp,type);
        }
        else
            alert('erro: ' + xhr.status +': '+ xhr.statusText)
    });
    console.info('Drawing '+type+' done.')
}



function draw_limits(type){
    if (type=='kml') 
        load_kml();
    /*
    else{
       $(document).load('get_limits/'+type, function(resp, status, xhr){
            if (status == 'success'){
                //alert('success: ' + resp);
                load_limits(resp,type);
            }
            else
                alert('erro: ' + xhr.status +': '+ xhr.statusText)
        });
    }
    */
    if(type=='json'){
        $.getJSON("get_limits/json", function(json) {
            ljson = json
            //console.log(ljson); // this will show the info it in firebug console
            load_limits(json,type)
        });
    }
}


$(document).ready(function(){

    

});
