module('site-local',
    imports(
        'lib.jquery'
    ),
    function($) {


    browserSucks = (jQuery.browser.msie && jQuery.browser.version < 8) ? true : false;
    browserSucksEggs = (jQuery.browser.msie && jQuery.browser.version < 7) ? true : false;


    jMod.ready(function() {
    	comments();
    	formDefaults();
    });
    


    function comments() {
    	var form = $('form.comment-form')
    	var inputs = form.find('textarea,input[type=text]')
	
    	inputs.each(function() {
    		var input = $(this)
    		var label = input.prev('label')
    		label.addClass('processed')
    		if(input.val() == '' && input.attr('name') != 'honeypot') {
    			input.val(label.html())
    		}
    	});
    }

    function formDefaults() {
    	var inputs = $('textarea,input[type=text]')
    	inputs.each(function() {
    		var input = $(this)
    		var defaultText = input.val()
    		input.focus(function() {
    			if(input.val() == defaultText) { input.val('') }
    		});
    		input.blur(function() {
    			if(input.val() == '' && input.attr('name') != 'honeypot') { input.val(defaultText) }
    		});
    	});
    }
    
    
});


