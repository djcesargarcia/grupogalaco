var map = L.map('map').setView([28.1184878,-15.453404], 15);
 
var tiles = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1
}).addTo(map);
 
  // Put markers in Leaflet
var marker = L.marker([28.11, -15.45]).addTo(map)
  .bindPopup('<b>Estoy en las torres.').openPopup();

  // Put popus in Leaflet
var popup = L.popup()
.setLatLng([28.11, -15.45])
.setContent('I am a standalone popup.')
.openOn(map);

function onMapClick(e) {
  popup
      .setLatLng(e.latlng)
      .setContent('You clicked the map at ' + e.latlng.toString())
      .openOn(map);
}

L.control.locate().addTo(map);
loadMap('map');