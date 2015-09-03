$(document).ready(
	function() {

	    var $payment = $("#payment_term");
	    $payment.on("change", function(ev) {
		var payment_term = $("#payment_term option:selected").val();		
		openerp.jsonRpc('/shop/payment_term/' + payment_term, 'call',
			{}).then(function(data) {
		    $form.submit();
		});
	    });
	});
