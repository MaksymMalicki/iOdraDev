// $(".div").click(function redirect_to_chunk(slug) {
//   var zoomTo = this.getAttribute("viewBox");
//   var slug = this.getAttribute("data")
//   $(".div").hide()
//   $(".navbar").hide()
//   $('.header').hide()
//   $('.scale').hide()
//   gsap.to("#svg128866", 1, {attr:{viewBox:zoomTo}, ease:"power3.inOut"})
//   window.setTimeout(function() {
//     window.location.href = "http://127.0.0.1:8000/map/"+slug+"/";
//     console.log()
//   }, 1000);
// })
$("html").click(function(e){
    var parentOffset = $(this).offset(); 
    var relX = e.pageX - parentOffset.left;
    var relY = e.pageY - parentOffset.top;
    var res = relX.toString() + " " + relY.toString()
    window.alert(res);
 });
