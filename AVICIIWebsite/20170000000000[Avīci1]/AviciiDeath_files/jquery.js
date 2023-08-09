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

(function($) {

  var self = this,
    container, running = false,
    currentY = 0,
    targetY = 0,
    oldY = 0,
    maxScrollTop = 0,
    minScrollTop, direction, onRenderCallback = null,
    fricton = 0.97, // higher value for slower deceleration
    vy = 0,
    stepAmt = 0.6,
    minMovement = 0.1,
    ts = 0.1;

  var updateScrollTarget = function(amt) {
    targetY += amt;
    vy += (targetY - oldY) * stepAmt;

    oldY = targetY;
  }
  var render = function() {
    if (vy < -(minMovement) || vy > minMovement) {

      currentY = (currentY + vy);
      if (currentY > maxScrollTop) {
        currentY = vy = 0;
      } else if (currentY < minScrollTop) {
        vy = 0;
        currentY = minScrollTop;
      }

      container.scrollTop(-currentY);

      vy *= fricton;

      if (onRenderCallback) {
        onRenderCallback();
      }
    }
  }
  var animateLoop = function() {
    if (!running) return;
    requestAnimFrame(animateLoop);
    render();
    //log("45","animateLoop","animateLoop", "",stop);
  }
  var onWheel = function(e) {
    e.preventDefault();
    var evt = e.originalEvent;

    var delta = evt.detail ? evt.detail * -1 : evt.wheelDelta / 40;
    var dir = delta < 0 ? -1 : 1;
    if (dir != direction) {
      vy = 0;
      direction = dir;
    }

    //reset currentY in case non-wheel scroll has occurred (scrollbar drag, etc.)
    currentY = -container.scrollTop();
    updateScrollTarget(delta);
  }

  /*
   * http://paulirish.com/2011/requestanimationframe-for-smart-animating/
   */
  window.requestAnimFrame = (function() {
    return window.requestAnimationFrame ||
      window.webkitRequestAnimationFrame ||
      window.mozRequestAnimationFrame ||
      window.oRequestAnimationFrame ||
      window.msRequestAnimationFrame ||
      function(callback) {
        window.setTimeout(callback, 1000 / 60);
      };
  })();

  /*
   * http://jsbin.com/iqafek/2/edit
   */
  var normalizeWheelDelta = function() {
    // Keep a distribution of observed values, and scale by the
    // 33rd percentile.
    var distribution = [],
      done = null,
      scale = 30;
    return function(n) {
      // Zeroes don't count.
      if (n == 0) return n;
      // After 500 samples, we stop sampling and keep current factor.
      if (done != null) return n * done;
      var abs = Math.abs(n);
      // Insert value (sorted in ascending order).
      outer: do { // Just used for break goto
        for (var i = 0; i < distribution.length; ++i) {
          if (abs <= distribution[i]) {
            distribution.splice(i, 0, abs);
            break outer;
          }
        }
        distribution.push(abs);
      } while (false);
      // Factor is scale divided by 33rd percentile.
      var factor = scale / distribution[Math.floor(distribution.length / 3)];
      if (distribution.length == 500) done = factor;
      return n * factor;
    };
  }();


  $.fn.smoothWheel = function() {
    //  var args = [].splice.call(arguments, 0);
    var options = jQuery.extend({}, arguments[0]);
    return this.each(function(index, elm) {

      if (!('ontouchstart' in window)) {
        container = $(this);
        container.bind("mousewheel", onWheel);
        container.bind("DOMMouseScroll", onWheel);

        //set target/old/current Y to match current scroll position to prevent jump to top of container
        targetY = oldY = container.scrollTop();
        currentY = -targetY;

        minScrollTop = container.get(0).clientHeight - container.get(0).scrollHeight;
        if (options.onRender) {
          onRenderCallback = options.onRender;
        }
        if (options.remove) {
          log("122", "smoothWheel", "remove", "");
          running = false;
          container.unbind("mousewheel", onWheel);
          container.unbind("DOMMouseScroll", onWheel);
        } else if (!running) {
          running = true;
          animateLoop();
        }

      }
    });
  };


})(jQuery);

}
/*
     FILE ARCHIVED ON 22:36:51 Apr 27, 2018 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 04:01:46 Jan 12, 2021.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  PetaboxLoader3.resolve: 143.612 (3)
  load_resource: 168.053 (2)
  PetaboxLoader3.datanode: 167.106 (5)
  captures_list: 182.777
  CDXLines.iter: 23.029 (3)
  exclusion.robots.policy: 0.17
  RedisCDXSource: 0.868
  exclusion.robots: 0.182
  esindex: 0.012
  LoadShardBlock: 152.982 (3)
*/