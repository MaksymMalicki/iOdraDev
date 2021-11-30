$(document).ready(function(){
  console.log(window.location.href)
  link = window.location.href
  if (link.includes("/map/")){
    $('.map-nav a').css("color","#023E73")
  }
  else if (link.includes("/map/") && str.length>19 ){
    $('.map-nav a').css("color","#023E73")
  }
  else if (link.includes("/komunikaty/")){
    $('.komunikaty-nav a').css("color","#023E73")
  }
  else if (link.includes("/sluzy/")){
    $('.sluzy-nav a').css("color","#023E73")
  }
  else if (link.includes("/contact/")){
    $('.telefony-nav a').css("color","#023E73")
  }
  else if (link.includes("/bezpieczenstwo/")){
    $('.water_safety-nav a').css("color","#023E73")
  }

  const idleDurationSecs = 60;
  const redirectUrl = '/';
  let idleTimeout;

  const resetIdleTimeout = function() {

      // Clears the existing timeout
      if(idleTimeout) clearTimeout(idleTimeout);

      // Set a new idle timeout to load the redirectUrl after idleDurationSecs
      idleTimeout = setTimeout(() => location.href = redirectUrl, idleDurationSecs * 1000);
  };

  // Init on page load
  resetIdleTimeout();

  // Reset the idle timeout on any of the events listed below
  ['click', 'touchstart', 'mousemove'].forEach(evt =>
      document.addEventListener(evt, resetIdleTimeout, false)
  );
});
