
jQuery(document).ready(function() {
	
    /*
        Fullscreen background
    */
    $.backstretch("../images/1.jpg");
    
    /*
        Form validation
    */
    $('.login-form input[type="text"], .login-form input[type="password"], .login-form textarea').on('focus', function() {
    	$(this).removeClass('input-error');
    });
    
    $('.login-form').on('submit', function(e) {
    	
    	$(this).find('input[type="text"], input[type="password"], textarea').each(function(){
    		if( $(this).val() == "" ) {
    			e.preventDefault();
    			$(this).addClass('input-error');
    		}
    		else {
    			$(this).removeClass('input-error');
    		}
    	});
    	
    });



    // jQuery('#addprop_submit').click(function(){
            
    //         var data = {'description':$('#addprop_prop').value(),
    //                     'price':$('#addprop_loc').value(),
    //                     'location':$('#addprop_price').value()};
    //         console.log("===========",data);
    //         $.ajax({url: '/login/addProperty/',
    //               type: 'POST',
    //               data: data, 
    //               success: function(result){
    //                 console.log(result.status,"success",result);
    //               },
    //               error: function(err){console.log(err,"error");}
    //             });

    //     });
    
    
});
