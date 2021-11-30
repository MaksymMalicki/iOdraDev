$('.info_block').click(function(){
    $(this).children(".info_container").find(".info_wrapper").slideToggle(250)
    $(this).children(".info_img").find(".infoimg").toggleClass('flip')
})
