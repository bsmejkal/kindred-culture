"use strict";

function showTribeDetails(evt) {
	evt.preventDefault();

	const inputName = $('#select-details').serialize();

	$.post('/details', (res) => {
		$('#show-details').html(`${res.name} ${res.region} ${res.description}`)
	});

}

$('#select-details').on('submit', showTribeDetails)