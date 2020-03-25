"use strict";

function showTribeDetails(evt) {
	evt.preventDefault();

	const inputName = $('#select-details').serialize();
	console.log(inputName);
	const formData = {"tribe_name": inputName};
	$.post('/details', formData, (res) => {
		console.log(res)
		$('#show-details').html(`${res.name} ${res.region} ${res.description}`)
	});

}

$('#select-details').on('submit', showTribeDetails);