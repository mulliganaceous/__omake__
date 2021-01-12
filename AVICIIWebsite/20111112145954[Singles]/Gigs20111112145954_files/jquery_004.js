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

$(document).ready(function(){
	// Index
	$('body.index #main-carousel').frontpageCarousel({
		
	});
	$('body.index a.close').live('click',function(e){
		var ajaxContainer = $('#ajax-wrapper');
		$('#media-wrapper #youtube').hide();
		ajaxContainer.slideUp();
	});
	$('body.index a.ajax-link').click(function(e){
		var anchor = $(this);
		
		if(anchor.attr('href').indexOf('/news/') >= 0){
		e.preventDefault();
		
		var ajaxContainer = $('#ajax-wrapper');
		
		$.ajax({
			url: anchor.attr('href'),
			method: 'get',
			data: {ajax:'ajax'},
			success: function(data){
				$('#media-wrapper #youtube').show();
				
				if(!ajaxContainer.is(':visible')){
					ajaxContainer.html(data);
					ajaxContainer.slideDown();
				}else{
					ajaxContainer.fadeIn('slow', function() {
						ajaxContainer.html(data);
					})
				}
				var clicky_goal_action ="";
				var clicky_custom = {};
				if(anchor.hasClass('top')){
					clicky_goal_action = "top";
					if(anchor.attr('data-orderNo') != '')
						clicky_goal_action = "top banner number:" + anchor.attr('data-orderNo');
				}else{
					clicky_goal_action = "bottom";
				}
				clicky.goal = { 'frontpage-banners': clicky_goal_action };
			}
		});
		}
	});
	
	//Avicii TV
	$('body.avicii-tv .clip-container').mouseenter(function(e){
		var title = $('.title', this);
		var play = $('.play', this);

		if($('.play').is(':visible'))
			$('.play').hide();

		if(!title.is(':visible')){
			title.slideDown('normal', function(){
			if(!play.is(':visible'))
				play.show();
			});
		}
	});
	$('body.avicii-tv .clip-container').mouseleave(function(e){
		var title = $('.title', this);
		var play = $('.play', this);

		if(title.is(':visible')){
			title.slideUp('fast', function(){
				play.hide();
			});
		}		
	});
	$('body.avicii-tv .clip-container').click(function(e){
		e.preventDefault;
		var container = $(this);
		var youtubeId = container.attr('data-youtubeId');
		container.html('<iframe width="280" height="210" src="http://web.archive.org/web/20130115163839/http://www.youtube.com/embed/' + youtubeId + '?autoplay=1" frameborder="0" autoplay allowfullscreen></iframe>')
	});
	// GIGS
	if($('body.gigs').length > 0){
		$('body.gigs #gig-list').jcarousel({
			vertical: true
			,scroll: 5
			//,wrap: "last"
		});
		$('body.gigs #gig-list li a').click(function(e){
			e.preventDefault();

			$('body.gigs #gig-list li a').removeClass('selected');
			$(this).addClass('selected');

			var ajaxUrl = $(this).attr('href');
			
			$.ajax({
				url: ajaxUrl,
				data: { ajax: 1},
				type: "GET",
				cache: false,
				success: function(data){
					$('.right-col .gig-wrapper').html(data);
					var script = 'http://web.archive.org/web/20130115163839/http://s7.addthis.com/js/250/addthis_widget.js#domready=1';
					if (window.addthis){
					    window.addthis = null;
					}
					$.getScript( script );
					if($('body.gigs #map').length > 0 && $('body.gigs #txtAddress').val() != ''){
						var mapScript = '/lib/javascript/gmap.js';
						$.getScript(mapScript);
					}

				},
				error: function(data){
					alert("We got ze error!");
				}
			})
		});
	}
	//Pictures
	if($('body.photos').length > 0){
		$("a.image").fancybox({
			'transitionIn'	:	'elastic',
			'transitionOut'	:	'elastic',
			'speedIn'		:	600, 
			'speedOut'		:	200, 
			'overlayShow'	:	false
		});
	}
});




}
/*
     FILE ARCHIVED ON 16:38:39 Jan 15, 2013 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 03:14:34 Jan 12, 2021.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  RedisCDXSource: 23.495
  exclusion.robots.policy: 0.183
  LoadShardBlock: 76.139 (3)
  exclusion.robots: 0.213
  PetaboxLoader3.datanode: 89.209 (4)
  load_resource: 52.608
  esindex: 0.013
  CDXLines.iter: 18.908 (3)
  PetaboxLoader3.resolve: 25.972
  captures_list: 121.472
*/