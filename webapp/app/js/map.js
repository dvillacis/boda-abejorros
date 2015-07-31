function initialize() {
	var mapOptions = {
		center: { lat: -1.232109, lng: -78.639045},
		zoom: 17,
		scrollwheel: false,
		streetViewControl: false
	};

	var map = new google.maps.Map(document.getElementById('map-canvas'),mapOptions);

	var marker = new google.maps.Marker({
		position: new google.maps.LatLng(-1.231528,-78.637686),
		map: map,
		title: 'Quinta San Martin'
	});
}
google.maps.event.addDomListener(window, 'load', initialize);