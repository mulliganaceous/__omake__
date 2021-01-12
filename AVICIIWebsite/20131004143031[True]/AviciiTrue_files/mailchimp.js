var _____WB$wombat$assign$function_____ = function(name) {return (self._wb_wombat && self._wb_wombat.local_init && self._wb_wombat.local_init(name)) || self[name]; };
if (!self.__WB_pmw) { self.__WB_pmw = function(obj) { this.__WB_source = obj; return this; } }
{
  let window = _____WB$wombat$assign$function_____("window");
  let self = _____WB$wombat$assign$function_____("self");
  let document = _____WB$wombat$assign$function_____("document");
  let location = _____WB$wombat$assign$function_____("location");
  let top = _____WB$wombat$assign$function_____("top");
  let parent = _____WB$wombat$assign$function_____("parent");
  let frames = _____WB$wombat$assign$function_____("frames");
  let opener = _____WB$wombat$assign$function_____("opener");

/* Form submission functions for the MailChimp Widget */
;(function($){
	$(function($) {
		// Change our submit type from HTML (default) to JS
		$('#mc_submit_type').val('js');
		
		// Attach our form submitter action
		$('#mc_signup_form').ajaxForm({
			url: mailchimpSF.ajax_url, 
			type: 'POST', 
			dataType: 'text',
			beforeSubmit: mc_beforeForm,
			success: mc_success
		});
	});
	
	function mc_beforeForm(){
		// Disable the submit button
		$('#mc_signup_submit').attr("disabled","disabled");
	}
	function mc_success(data){
		// Re-enable the submit button
		$('#mc_signup_submit').removeAttr("disabled");
		
		// Put the response in the message div
		$('#mc_message').html(data);
		
		// See if we're successful, if so, wipe the fields
		var reg = new RegExp("class='mc_success_msg'", 'i');
		if (reg.test(data)){
			$('.mc_custom_border_hdr, .mc_merge_var, .mc_signup_submit').hide();
			$('#mc_signup_form').each(function(){
				this.reset();
			});
			$('#mc_submit_type').val('js');
		}
		$.scrollTo('#mc_signup', {offset: {top: -28}});
	}
})(jQuery);


}
/*
     FILE ARCHIVED ON 00:57:48 Oct 06, 2013 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 03:29:14 Jan 12, 2021.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  captures_list: 264.395
  exclusion.robots: 0.085
  exclusion.robots.policy: 0.079
  RedisCDXSource: 1.564
  esindex: 0.008
  LoadShardBlock: 246.64 (3)
  PetaboxLoader3.datanode: 259.414 (4)
  CDXLines.iter: 13.883 (3)
  load_resource: 78.55
  PetaboxLoader3.resolve: 32.332
*/