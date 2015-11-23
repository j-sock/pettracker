function toggleDone(checkboxElement) {
	var checkbox = $(checkboxElement)[0];
	$.ajax({
		url: '/pets/tasks/' + checkbox.value + '/check/',
		type: 'POST',
		data: { done: checkbox.checked },
		success: function(json) {
			console.log(json);
		},
		error: function(xhr, errmsg, err) {
			console.log(xhr.status + ": " + xhr.responseText);
		}
	});
}
