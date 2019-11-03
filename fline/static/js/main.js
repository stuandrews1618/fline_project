const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// $( "#message_id" ).fadeIn( 1000 ).delay( 1500 ).fadeOut(1500);

// setTimeout(function(){$('#message_id').fadeOut();}, 1000);


setTimeout(function() {
    $('#alert_message').fadeOut('slow');
}, 2000);

// setTimeout(() => {
//     $('#message').fadeOut('slow');
// }, 3000);