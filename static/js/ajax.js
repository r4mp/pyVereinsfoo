$(function() {
	
	$('#search').keyup(function() {
		$.ajax({
			type: "POST",
			url: "/members/search/",
			data: {
				'search_string': $('#search').val(),
				'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
			},
			success: searchSuccess,
			dataType: 'html'
		})
	});

});

function searchSuccess(data, textStatus, jqXHR) {
	$('#search-results').html(data);
}
