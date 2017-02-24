function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 6,
    center: {lat: 54.8, lng: -3},
    //https://snazzymaps.com/style/8097/wy
    styles: [{"featureType":"all","elementType":"geometry.fill","stylers":[{"weight":"2.00"}]},{"featureType":"all","elementType":"geometry.stroke","stylers":[{"color":"#9c9c9c"}]},{"featureType":"all","elementType":"labels.text","stylers":[{"visibility":"on"}]},{"featureType":"landscape","elementType":"all","stylers":[{"color":"#f2f2f2"}]},{"featureType":"landscape","elementType":"geometry.fill","stylers":[{"color":"#ffffff"}]},{"featureType":"landscape.man_made","elementType":"geometry.fill","stylers":[{"color":"#ffffff"}]},{"featureType":"poi","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"all","stylers":[{"saturation":-100},{"lightness":45}]},{"featureType":"road","elementType":"geometry.fill","stylers":[{"color":"#eeeeee"}]},{"featureType":"road","elementType":"labels.text.fill","stylers":[{"color":"#7b7b7b"}]},{"featureType":"road","elementType":"labels.text.stroke","stylers":[{"color":"#ffffff"}]},{"featureType":"road.highway","elementType":"all","stylers":[{"visibility":"simplified"}]},{"featureType":"road.arterial","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"water","elementType":"all","stylers":[{"color":"#46bcec"},{"visibility":"on"}]},{"featureType":"water","elementType":"geometry.fill","stylers":[{"color":"#c8d7d4"}]},{"featureType":"water","elementType":"labels.text.fill","stylers":[{"color":"#070707"}]},{"featureType":"water","elementType":"labels.text.stroke","stylers":[{"color":"#ffffff"}]}]

  });

  // Create an array of alphabetical characters used to label the markers.
  var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  var data = [751500, 2550000, 198051, 2540, 1450000, 8674000, 226841, 109805, 256400, 341000, 33837, 10887, 3949, 22834, 21646, 625698, 551800, 13213, 2196000, 150200, 11805]

  // Add some markers to the map.
  // Note: The code uses the JavaScript Array.prototype.map() method to
  // create an array of markers based on a given "locations" array.
  // The map() method here has nothing to do with the Google Maps API.
  var markers = locations.map(function(location, i) {
    return new google.maps.Marker({
      position: location,
      label: "Fl", //labels[i % labels.length]
      title: data[i].toString()
    });
  });

  // Add a marker clusterer to manage the markers.
  var markerCluster = new MarkerClusterer(map, markers,
      {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});

  for (var i = 0; i < markers.length; i++) {
    pop_value = data[i].toString()
    var infowindow =  new google.maps.InfoWindow({
        content: 'Population: ' + pop_value
      });
    markers[i].addListener('mouseover', function() {
        infowindow.setContent('Population: ' + this.title)
        infowindow.open(map, this);
    });

    // assuming you also want to hide the infowindow when user mouses-out
    markers[i].addListener('mouseout', function() {
        infowindow.close();
    });
  }
}

var locations = [{lng: -1.5490774, lat: 53.8007554}, {lng: -2.2426305, lat: 53.4807593}, {lng: -76.727745, lat: 39.9625984}, {lng: -73.85823979999999, lat: 41.1115447}, {lng: -76.3055144, lat: 40.0378755}, {lng: -0.1277583, lat: 51.5073509}, {lng: -0.1356583, lat: 51.4974948}, {lng: -1.128462, lat: 53.52282}, {lng: -70.6672621, lat: 41.9584457}, {lng: -3.17909, lat: 51.48158100000001}, {lng: -0.198802, lat: 54.08535}, {lng: -111.8389726, lat: 40.5649781}, {lng: -1.9837091, lat: 53.7309278}, {lng: -75.12933509999999, lat: 42.1695296}, {lng: -106.7234639, lat: 39.576406}, {lng: -0.399752, lat: 54.283113}, {lng: -1.470085, lat: 53.38112899999999}, {lng: -0.613347, lat: 54.486335}, {lng: -95.3698028, lat: 29.7604267}, {lng: -1.2577263, lat: 51.7520209}, {lng: -117.0693286, lat: 46.3994763}]