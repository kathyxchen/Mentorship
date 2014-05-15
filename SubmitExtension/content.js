function fillButtons() {
	var hours = '';
	for (var i = 1; i <= 12; i++) {
		hours += '<option>' + i + '</option>'
	}
	$('#hour').append(hours)
	var mins = '';
	for (var i = 15; i <= 60; i += 15) {
		mins += '<option>' + i + '</option>'
	}
	$('#mins').append(mins)
}

function submit() {
	
    
	$('#submit').click(function(event){
		var regex = /\S+@\S+\.\S+/;
		var emailaddr = $('#email').val();
		var mon = $('#month').val();
		var day = $('#day').val();
		var yr = $('#year').val();

   		if(mon == '' || day == '' || yr == '' 
   			|| emailaddr == ''){
      		$('.errors').text('Input cannot be left blank');
        	$('.errors').show();
        	$('.errors').fadeOut(2500);
      		return false;
   		}
   		else if (!(regex.test(emailaddr))){
   			
        	$('.errors').text('Please insert a valid email');
        	$('.errors').show();
        	$('.errors').fadeOut(2500);
        	return false;
    	} 

    	else if (!($.isNumeric(mon)) || !($.isNumeric(day))
    		|| !($.isNumeric(yr))) {
    			$('.errors').text('Dates must be numbers');
        		$('.errors').show();
        		$('.errors').fadeOut(2500);
        		return false;
    		}

    	else if (mon.length > 2 || day.length > 2 || yr.length > 4) {
    			$('.errors').text('Invalid Date');
        		$('.errors').show();
        		$('.errors').fadeOut(2500);
        		return false;
    		}

   		else{
   			var params = {'email': $('#email').val(), 'mon':$('#month').val(), 'day':$('#day').val(), 'yr':$('#year').val(), 
			'hr': $('#hour').val(), 'mins':$('#mins').val(), 'ampm':$('#ampm').val()};

			$.post('http://localhost:5000/schedule',params,function(e) { console.log(e); });
   			
        /*if(!confirm('Paper submission sending to ' + $('#email').val() 
   			+ ' on ' + $('#month').val() + '/' + $('#day').val() + '/' +
   			$('#year').val() + ' at ' + $('#hour').val() + ':' + $('#mins').val() + $('#ampm').val() + '.')) {
        	event.preventDefault();
        	return;
    		}*/
    		
        $('.document').text('Paper submission sending to ' + emailaddr 
   			+ ' on ' + mon + '/' + day + '/' + yr + ' at ' + $('#hour').val() 
   			+ ':' + $('#mins').val() + $('#ampm').val() + '.');
   			$('.document').show();
            $('.document').fadeOut(2500);
        }

	});
}

$(document).ready(function() {
	fillButtons();
	submit();

});