"use strict";

function showTribeDetails(evt) {
	evt.preventDefault();

	const inputName = $('#select-details').serialize();

	$.post('/details', inputName, (res) => {
		$('#show-name').html(`${res.name}`)
	});

	$.post('/details', inputName, (res) => {
		$('#show-region').html(`${res.region}`)
	});

	$.post('/details', inputName, (res) => {
		$('#show-description').html(`${res.description}`)
	});

}

$('#select-details').on('submit', showTribeDetails);