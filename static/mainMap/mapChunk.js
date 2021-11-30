$(".sluza").click(function(){
  var slug = $(this).attr("data")
  $.ajax({
  type: 'GET',
  url: '/sluza/'+slug,
  data: {'slug':slug},
  success: function(data){
    $(".info").css("display", "block")
    $(".info").html(`
      <div class="info-sub non-blur">
        <div class="left non-blur">
          <div class="inline-chunk">
            <span id="marina-filter" class="marina-checkbox checkbox"><p>Ś</p></span>
            <p class="object_title">`+data['name']+`</p>
          </div>
          <div class="object_image" style="width: 80%; min-height: 200px; margin: 20px auto; background-position: center center; background-image: url('`+data['img']+`'); background-repeat: no-repeat; background-size: cover;">

          </div>
        </div>
        <div class="right non-blur">
          <div class="close" style="text-align: right; margin-top: -5px;">
            <img class="close-img" src="/static/website_images/quit_icon.png" alt="QUIT">
          </div>
          <p class="object_info1">
            `+data['localization']+`</p>
          <p class="object_info2">
            `+data['dimensions']+`
          </p>
          <p class="object_info3">`+data['contact']+`</p>
        </div>
      </div>
      <p class="info4 non-blur">
        `+data['distance']+`
      </p>
    `)
    var div = document.getElementsByClassName("close-img")[0];
    var modal = document.getElementById("info");
    div.onclick = function(event){
      $(".info").css("display","none")
    }
  }})
})

$(".marina").click(function(){
  var slug = $(this).attr("data")
  $.ajax({
  type: 'GET',
  url: '/marina/'+slug,
  data: {'slug':slug},
  success: function(data){
    $(".info").css("display", "block")
    $(".info").html(`
      <div class="info-sub non-blur">
        <div class="left non-blur">
          <div class="inline-chunk">
            <span id="marina-filter" class="marina-checkbox checkbox"><p>M</p></span>
            <p class="object_title">`+data['name']+`</p>
          </div>
          <div class="object_image" style="width: 80%; min-height: 200px; margin: 20px auto; background-position: center center; background-image: url('`+data['img']+`'); background-repeat: no-repeat; background-size: cover;">

          </div>
        </div>
        <div class="right non-blur">
          <div class="close" style="text-align: right; margin-top: -5px;">Zamykanie</div>
          <p class="object_info1">
            `+data['localization']+`</p>
          <p class="object_info2">
            `+data['dimensions']+`
          </p>
          <p class="object_info3">`+data['contact']+`</p>
        </div>
      </div>
      <p class="info4 non-blur">
        `+data['distance']+`
      </p>
    `)
    var div = document.getElementsByClassName("close")[0];
    var modal = document.getElementById("info");
    div.onclick = function(event){
      $(".info").css("display","none")
    }
  }})
})

$(".jaz").click(function(){
  var slug = $(this).attr("data")
  $.ajax({
  type: 'GET',
  url: '/jaz/'+slug,
  data: {'slug':slug},
  success: function(data){
    $(".info").css("display", "block")
    $(".info").html(`
      <div class="info-sub non-blur">
        <div class="left non-blur">
          <div class="inline-chunk">
            <span id="marina-filter" class="marina-checkbox checkbox"><p>J</p></span>
            <p class="object_title">`+data['name']+`</p>
          </div>
          <div class="object_image" style="width: 80%; min-height: 200px; margin: 20px auto; background-position: center center; background-image: url('`+data['img']+`'); background-repeat: no-repeat; background-size: cover;">

          </div>
        </div>
        <div class="right non-blur">
          <div class="close" style="text-align: right; margin-top: -5px; cursor: pointer;">Zamykanie</div>
          <p class="object_info1">
            `+data['localization']+`</p>
          <p class="object_info2">
            `+data['dimensions']+`
          </p>
          <p class="object_info3">`+data['contact']+`</p>
        </div>
      </div>
      <p class="info4 non-blur">
        `+data['distance']+`
      </p>
    `)
    var div = document.getElementsByClassName("close")[0];
    var modal = document.getElementById("info");
    div.onclick = function(event){
      $(".info").css("display","none")
    }
  }})
})


$('#lock-filter').click(function(){
    $(this).toggleClass("lock-checkbox")
    if($(this).hasClass("lock-checkbox")){
      $('.sluza').each(function(){
        $(this).show()
      })
      $("#lock-filter p").show()
    }
    else{
      $('.sluza').each(function(){
        $(this).hide()
      })
      $("#lock-filter p").hide()
    }
})

$('#marina-filter').click(function(){
    $(this).toggleClass("marina-checkbox")
    if($(this).hasClass("marina-checkbox")){
      $('.marina').each(function(){
        $(this).show()
      })
      $("#marina-filter p").show()
    }
    else{
      $('.marina').each(function(){
        $(this).hide()
      })
      $("#marina-filter p").hide()
    }
})

$('#weir-filter').click(function(){
    $(this).toggleClass("weir-checkbox")
    if($(this).hasClass("weir-checkbox")){
      $('.jaz').each(function(){
        $(this).show()
      })
      $("#weir-filter p").show()
    }
    else{
      $('.jaz').each(function(){
        $(this).hide()
      })
      $("#weir-filter p").hide()
    }
})
