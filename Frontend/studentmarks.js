$(document).ready(function(){
    $('#totalmarks').on('click', function(){
	alert('WORKING SUCCESSFULLY');
        $.ajax({
            url:"/sum",
            type:"GET",
            
            success: function (data) {
                alert('woohoo success');
            },
            error: function(data) {
                alert("something's wrong");
            }
        })
	});
});









