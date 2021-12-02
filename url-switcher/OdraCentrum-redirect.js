// console.log("Przekierowanie nastąpi za 30 sekund")
// window.setTimeout(function(){
    // window.location.href = "http://127.0.0.1:8000/"
// }, 30000)

var id;

function redirectAfterIdle(){
    console.log("wystartowano zegar!")
    id = window.setTimeout(function(){
        window.location.href = "http://127.0.0.1:8000/"
    }, 30000)
}

function resetWait(){
    clearTimeout(id)
    redirectAfterIdle();
}

function setWait(){
    document.addEventListener("touchstart", resetWait, false);
    document.addEventListener("touchend", resetWait, false);
    document.addEventListener("touchcancdocument", resetWait, false);
    document.addEventListener("touchmove", resetWait, false);
    document.addEventListener("wheel", resetWait, false);
    document.addEventListener("click", resetWait, false)
}

redirectAfterIdle()
setWait()

document.getElementsByClassName('facebook')[0].href="";
document.getElementsByClassName('instagram')[0].href="";
document.getElementsByClassName('email')[0].href="";


