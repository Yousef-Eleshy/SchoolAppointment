$(document).ready(function(){
	$( '.wpforms-field-radio .wpforms-image-choices-item input:checked' ).change();
    
    // Error Messages for blank fields (Mandatory Page 1 fields)
	$('#page11').click(function(e) {
		var first_name = $('#wpforms-4201-field_141').val();
		var last = $('#wpforms-4201-field_141-last').val();
		var email = $('#wpforms-4201-field_142').val();
		var confirm_email = $('#wpforms-4201-field_142-secondary').val();
		var phone = $('#wpforms-4201-field_140-phone').val();
		var choose = $("input[type=radio]").val()
		if (first_name === '') {
			$('#wpforms-4201-field_141').after('<span class="error">Please enter your First Name</span>');
	        return false;
	    }
	    if (last === '') {
			$('#wpforms-4201-field_141-last').after('<span class="error">Please enter your Last Name</span>');
	        
	        return false;
	    }
	    if (email === '') {
			$('#wpforms-4201-field_142').after('<span class="error">Please enter your Email</span>');
	        return false;
	    }
	    if (confirm_email === '') {
			$('#wpforms-4201-field_142-secondary').after('<span class="error">Please Confirm your Email</span>');
	        return false;
	    }
	    if (phone === '') {
			$('#wpforms-4201-field_140-phone').after('<span class="error">Please enter your Mobile Number</span>');
	        return false;
	    }
	    if (choose === '') {
			$('input[type=radio]').after('<span class="error">This field is required</span>');
	        
	        return false;
	    }
        // Page 1 to Page 2
		$('.wpforms-page-1').hide();
		$('.wpforms-page-2').show();
	    });

$(document).ready(function(){
        // Page 2 to Page 1
		$('#page_prev').click(function(e) {
			$('.wpforms-page-1').show();
			$('.wpforms-page-2').hide();				
			});	

    // Page 2 to Page 3
	$('#page12').click(function(e) {
		$('.wpforms-page-2').hide();
		$('.wpforms-page-3').show();
	});
    // Page 3 to Page 4
	$('#page13').click(function(e) {
		$('.wpforms-page-3').hide();
		$('.wpforms-page-4').show();
	});
    // Page 3 to Page 2
	$('#page13_prev').click(function(e) {
		$('.wpforms-page-3').hide();
		$('.wpforms-page-2').show();	
	});
   	// Page 4 to Page 5 	
   	$('#page14').click(function(e) {	   
		$('.wpforms-page-4').hide();
		$('.wpforms-page-5').show();					
   	});
   	// Page 4 to Page 3 	
	$('#page14_prev').click(function(e) {
		$('.wpforms-page-4').hide();
		$('.wpforms-page-3').show();		
   	});
    // Page 5 to Page 4
   	$('#page15_prev').click(function(e) {
		$('.wpforms-page-4').show();
		$('.wpforms-page-5').hide();		
	});
});



	$( '.wpforms-field-radio .wpforms-image-choices-item input:checked' ).change();
} );

$( document ).on( 'change', '.wpforms-field-checkbox input, .wpforms-field-radio input, .wpforms-field-payment-multiple input, .wpforms-field-payment-checkbox input, .wpforms-field-gdpr-checkbox input', function( event ) {

	var $this  = $( this ),
		$field = $this.closest( '.wpforms-field' );

	if ( $field.hasClass( 'wpforms-conditional-hide' ) ) {
		event.preventDefault();
		return false;
	}
	switch ( $this.attr( 'type' ) ) {
		case 'radio':
			$this.closest( 'ul' ).find( 'li' ).removeClass( 'wpforms-selected' ).find( 'input[type=radio]' ).removeProp( 'checked' );
			$this
				.prop( 'checked', true )
				.closest( 'li' ).addClass( 'wpforms-selected' );
			break;

		case 'checkbox':
			if ( $this.prop( 'checked' ) ) {
				$this.closest( 'li' ).addClass( 'wpforms-selected' );
				$this.prop( 'checked', true );
			} else {
				$this.closest( 'li' ).removeClass( 'wpforms-selected' );
				$this.removeProp( 'checked' );
			}
			break;
	}
} );

//when submitted if there was an issue
 $("form input").on("invalid", function() {
    $(this).parents('.wpforms-container').find('.div').show()
});

// Conditional Fields - Show/Hide Sub-Fields based on Condition 
$(document).ready(function() {
    // Student - Egyptian 
	$("#wpforms-4201-field_54_1").click(function(e){
        // National ID
		$('#wpforms-4201-field_31-container').show()
        // Passport Number
		$('#wpforms-4201-field_60-container').hide()
	});
    // Student - Non-Egyptian
	$("#wpforms-4201-field_54_2").click(function(e){
        // Passport Number
		$('#wpforms-4201-field_60-container').show()
        // National ID
		$('#wpforms-4201-field_31-container').hide()
	});
    // Father - Egyptian
	$("#wpforms-4201-field_149_1").click(function(e){
        // National ID
		$('#wpforms-4201-field_150-container').show()
        // Passport Number
		$('#wpforms-4201-field_151-container').hide()
	});
    // Father - Non-Egyptian
	$("#wpforms-4201-field_149_2").click(function(e){
        // Passport Number
		$('#wpforms-4201-field_151-container').show()
        // National ID
		$('#wpforms-4201-field_150-container').hide()
	});
    // Mother Egyptian
	$("#wpforms-4201-field_157_1").click(function(e){
        // National ID
		$('#wpforms-4201-field_158-container').show()
        // Passport Number
		$('#wpforms-4201-field_159-container').hide()
	});
    // Mother - Non-Egyptian
	$("#wpforms-4201-field_157_2").click(function(e){
        // Passport Number
		$('#wpforms-4201-field_159-container').show()
        // National ID
		$('#wpforms-4201-field_158-container').hide()
	});
    // Mother - Martital Status - Divorced 
	$("#wpforms-4201-field_165_2").click(function(e){
        // Legal Guardian
		$('#wpforms-4201-field_92-container').show()
	});
    // Mother - Martital Status - Married
	$("#wpforms-4201-field_165_1").click(function(e){
        // Legal Guardian - Hide
		$('#wpforms-4201-field_92-container').hide()
	});
    // Mother - Martital Status - Widow
	$("#wpforms-4201-field_165_3").click(function(e){
        // Legal Guardian 
		$('#wpforms-4201-field_92-container').show()
	});
    // Applicant's Siblings - YES
	$("#wpforms-4201-field_107_1").click(function(e){
        // Sibling Name
		$('#wpforms-4201-field_108-container').show()
        // Sibling Grade Level
		$('#wpforms-4201-field_110-container').show()
        // Sibling School
		$('#wpforms-4201-field_167-container').show()


	});
    // Applicant's Siblings - NO
	$("#wpforms-4201-field_107_2").click(function(e){
		// Sibling Name
		$('#wpforms-4201-field_108-container').hide()
        // Sibling Grade Level
		$('#wpforms-4201-field_110-container').hide()
        // Sibling School
		$('#wpforms-4201-field_167-container').hide()
	});
    // Educational System - American
	$("#wpforms-4201-field_49_1").click(function(e){
        // American Grade-Levels
		$('#wpforms-4201-field_138-container').show()
        // British Grade-Levels
		$('#wpforms-4201-field_139-container').hide()
	});
    // Educational System - British
	$("#wpforms-4201-field_49_2").click(function(e){
        // British Grade-Levels
		$('#wpforms-4201-field_139-container').show()
        // American Grade-Levels
		$('#wpforms-4201-field_138-container').hide()

	});
    // Legal Guardian - Other
	$("#wpforms-4201-field_92_3").click(function(e){
        // Type Other Legal Guardian
		$('#wpforms-4201-field_93-container').show()
	});
    // Student Second Language - Other
	$("#wpforms-4201-field_59_3").click(function(e){
        // Please Specify Other
		$('#wpforms-4201-field_144-container').show()
	});
    // Does your child require special accommodation - Yes
	$("#wpforms-4201-field_146_1").click(function(e){
        // Please Specify
		$('#wpforms-4201-field_41-container').show()
	});
    // Does your child require special accommodation - No
	$("#wpforms-4201-field_146_2").click(function(e){
        // Please Specify
		$('#wpforms-4201-field_41-container').hide()
	});
    // Previous School/Nursery - Other
	$("#wpforms-4201-field_57_4").click(function(e){
        // Please Specify
		$('#wpforms-4201-field_58-container').show()
	});

});

// Skip Pages
$(document).ready(function() {
	// $('#skip_42011').click(function(e) {
	// 	$('.wpforms-page-1').hide();
	// 	$('.wpforms-page-2').show();				

	//    	});
    
        // Skip from Page 2 to Page 3
	   	$('#skip_42012').click(function(e) {
			$('.wpforms-page-2').hide();
			$('.wpforms-page-3').show();		

	   	});
        // Skip from Page 3 to Page 4
	   	$('#skip_42013').click(function(e) {
			$('.wpforms-page-3').hide();
			$('.wpforms-page-4').show();		
	   	});
        // Skip from Page 4 to Page 5
	   	$('#skip_42014').click(function(e) {
			$('.wpforms-page-4').hide();
			$('.wpforms-page-5').show();		
	   	});

});