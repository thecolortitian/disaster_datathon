 function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 6,
    center: {lat: 54.8, lng: -3},
    //https://snazzymaps.com/style/8097/wy
    styles: [{"featureType":"all","elementType":"geometry.fill","stylers":[{"weight":"2.00"}]},{"featureType":"all","elementType":"geometry.stroke","stylers":[{"color":"#9c9c9c"}]},{"featureType":"all","elementType":"labels.text","stylers":[{"visibility":"on"}]},{"featureType":"landscape","elementType":"all","stylers":[{"color":"#f2f2f2"}]},{"featureType":"landscape","elementType":"geometry.fill","stylers":[{"color":"#ffffff"}]},{"featureType":"landscape.man_made","elementType":"geometry.fill","stylers":[{"color":"#ffffff"}]},{"featureType":"poi","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"all","stylers":[{"saturation":-100},{"lightness":45}]},{"featureType":"road","elementType":"geometry.fill","stylers":[{"color":"#eeeeee"}]},{"featureType":"road","elementType":"labels.text.fill","stylers":[{"color":"#7b7b7b"}]},{"featureType":"road","elementType":"labels.text.stroke","stylers":[{"color":"#ffffff"}]},{"featureType":"road.highway","elementType":"all","stylers":[{"visibility":"simplified"}]},{"featureType":"road.arterial","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"water","elementType":"all","stylers":[{"color":"#46bcec"},{"visibility":"on"}]},{"featureType":"water","elementType":"geometry.fill","stylers":[{"color":"#c8d7d4"}]},{"featureType":"water","elementType":"labels.text.fill","stylers":[{"color":"#070707"}]},{"featureType":"water","elementType":"labels.text.stroke","stylers":[{"color":"#ffffff"}]}]

  });

  // Create an array of alphabetical characters used to label the markers.
  var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

  // Add some markers to the map.
  // Note: The code uses the JavaScript Array.prototype.map() method to
  // create an array of markers based on a given "locations" array.
  // The map() method here has nothing to do with the Google Maps API.
  var markers = locations.map(function(location, i) {
    return new google.maps.Marker({
      position: location,
      label: labels[i % labels.length]
    });
  });

  // Add a marker clusterer to manage the markers.
  var markerCluster = new MarkerClusterer(map, markers,
      {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
}

var locations = [
{lat: 51.4974948, lng: -0.1356583}, 
{lat: 43.57596729999999, lng: -91.2258583}, 
{lat: 51.48158100000001, lng: -3.17909}, 
{lat: 53.806051, lng: -2.359046}, 
{lat: 53.4807593, lng: -2.2426305}, 
{lat: 53.8007554, lng: -1.5490774}, 
{lat: 53.806051, lng: -2.359046}, 
{lat: 54.32800599999999, lng: -2.74629}, 
{lat: 51.4974948, lng: -0.1356583}, 
{lat: 51.5073509, lng: -0.1277583}, 
{lat: 29.9118885, lng: -95.0621512}, 
{lat: 51.4974948, lng: -0.1356583}, 
{lat: 51.2296539, lng: -3.840102}, 
{lat: 51.5073509, lng: -0.1277583}, 
{lat: 33.1565939, lng: -91.7538817},
{lat: 53.8007554, lng: -1.5490774}, 
{lat: 53.4807593, lng: -2.2426305}, 
{lat: 53.806051, lng: -2.359046}, 
{lat: 51.7520209, lng: -1.2577263}, 
{lat: 40.0378755, lng: -76.3055144}, 
{lat: 39.9625984, lng: -76.727745}, 
{lat: 41.1815863, lng: -101.5248055}, 
{lat: 29.7604267, lng: -95.3698028}, 
{lat: 55.070859, lng: -3.60512}, 
{lat: 55.953252, lng: -3.188267}, 
{lat: 55.38747, lng: -4.001596}, 
{lat: 31.7162882, lng: -94.60493129999999}, 
{lat: 40.2010241, lng: -77.20027449999999}, 
{lat: 53.806051, lng: -2.359046}, 
{lat: 54.32800599999999, lng: -2.74629}, 
{lat: 40.0378755, lng: -76.3055144}, 
{lat: 46.9529785, lng: -114.1215023}, 
{lat: 44.9204669, lng: -115.7926381}, 
{lat: 53.716344, lng: -2.0987969}, 
{lat: 53.822643, lng: -2.407684},
{lat: 53.7309278, lng: -1.9837091}, 
{lat: 31.4881376, lng: -97.1363507}, 
{lat: 53.699729, lng: -1.782501}, 
{lat: 53.795984, lng: -1.759398}, 
{lat: 53.871098, lng: -2.393083}, 
{lat: 53.595502, lng: -1.382954}, 
{lat: 35.0241873, lng: -110.6973571}, 
{lat: 53.6097136, lng: -2.1561}, 
{lat: 53.806051, lng: -2.359046}, 
{lat: 51.62144, lng: -3.943645999999999}, 
{lat: 43.57596729999999, lng: -91.2258583}, 
{lat: 39.9625984, lng: -76.727745}, 
{lat: 53.806051, lng: -2.359046}, 
{lat: 53.9371762, lng: -1.0688195}, 
{lat: 52.312938, lng: 0.016875}, 
{lat: 51.5073509, lng: -0.1277583}, 
{lat: 39.9625984, lng: -76.727745}, 
{lat: 42.1695296, lng: -75.12933509999999}, 
{lat: 53.52282, lng: -1.128462}, 
{lat: 54.486335, lng: -0.613347}, 
{lat: 53.7309278, lng: -1.9837091}, 
{lat: 54.283113, lng: -0.399752}, 
{lat: 54.08535, lng: -0.198802}, 
{lat: 51.5073509, lng: -0.1277583}, 
{lat: 41.9584457, lng: -70.6672621}, 
{lat: 39.576406, lng: -106.7234639}, 
{lat: 53.8007554, lng: -1.5490774}, 
{lat: 30.6749425, lng: -97.58617009999999}, 
{lat: 52.551716, lng: 0.08862199999999999}]