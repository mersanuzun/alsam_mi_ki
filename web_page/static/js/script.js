$(document).ready(function() {
    $('#search-button').on('click', function(){
        var link = $("#link").val()
        if (link == ""){
	   $('#search-error')
			.css('visibility', 'visible')
			.html('<h4><b>Product link is not be empty.</b></h4>')
	    return false
        }
    });
});

