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

$.fn.frontpageCarousel=function(a){var b;var c=$.extend({arrowClass:"large-arrow",backgroundArrow:"large-arrow-bg",startPage:1,offset:0,tabs:false,tabSelector:".tabs",transitionSpeed:7e3},a);return this.each(function(){function o(){clearTimeout(b);b=setTimeout(function(){n(j+1)},c.transitionSpeed)}function n(a){if(a>m)a=1;else if(a<1)a=m;e.stop();var b=a-1;j=parseInt(a,10);var d=h*b;if(c.tabs){l.removeClass("selected");l.eq(a-1).addClass("selected")}e.filter(":not(:animated)").animate({left:-d},900,"easeOutQuint",function(){});o();return false}var a=$(this).css("overflow","hidden"),d=a.find("> div"),e=d.find("> ul"),f=e.find("> li"),g=f.filter(":first"),h=g.outerWidth(),i=Math.ceil(a.innerWidth()/h),j=c.startPage,k=Math.ceil(f.length);if(c.tabs){var l=$(c.tabSelector);l.eq(j-1).addClass("selected")}var m=f.length;e.css("width",h*m);e.before('<div class="'+c.backgroundArrow+' back"></div><div class="'+c.backgroundArrow+' forward"></div>');e.after('<div class="'+c.arrowClass+' back"></div><div class="'+c.arrowClass+' forward"></div>');$(".item img",this).mouseenter(function(){clearTimeout(b)});$(".item img",this).mouseleave(function(){o()});$("div.back",this).click(function(){return n(j-1)});$("div.forward",this).click(function(){return n(j+1)});o();$(this).bind("goto",function(a,b){n(b)})})}

}
/*
     FILE ARCHIVED ON 16:38:39 Jan 15, 2013 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 03:14:33 Jan 12, 2021.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  LoadShardBlock: 59.49 (3)
  PetaboxLoader3.datanode: 67.639 (4)
  CDXLines.iter: 23.175 (3)
  RedisCDXSource: 0.75
  exclusion.robots: 0.201
  load_resource: 74.97
  esindex: 0.015
  PetaboxLoader3.resolve: 22.298
  exclusion.robots.policy: 0.187
  captures_list: 87.472
*/