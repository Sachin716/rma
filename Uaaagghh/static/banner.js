let i1 = document.querySelector(".image1")
let i2 = document.querySelector(".image2")
let i3 = document.querySelector(".image3")
let i4 = document.querySelector(".image4")
let i5 = document.querySelector(".image5")
let i6 = document.querySelector(".image6")





function banner1(){
    setTimeout(function(){
        i1.style.width = "0%"
        i2.style.width = "100%"
        i2.style.left = "0%"
        i6.style.left = "100%"
        banner2()
    },2000)
}
function banner2(){
    setTimeout(function(){
        i2.style.width = "0%"
        i3.style.width = "100%"
        i3.style.left = "0%"
        i1.style.left = "100%"
        banner3()
    },2000)
}
function banner3(){
    setTimeout(function(){
        i3.style.width = "0%"
        i4.style.width = "100%"
        i4.style.left = "0%"
        i2.style.left = "100%"
        banner4()
    },2000)
}
function banner4(){
    setTimeout(function(){
        i4.style.width = "0%"
        i5.style.width = "100%"
        i5.style.left = "0%"
        i3.style.left = "100%"
        banner5()
    },2000)
}
function banner5(){
    setTimeout(function(){
        i5.style.width = "0%"
        i6.style.width = "100%"
        i6.style.left = "0%"
        i4.style.left = "100%"
        banner6()
            },2000)
}
function banner6(){
    setTimeout(function(){
        i6.style.width = "0%"
        i1.style.width = "100%"
        i1.style.left = "0%"
        i5.style.left = "100%"
        banner1()
    },2000)
}


function banner_mob1(){
    setTimeout(function(){
        i1.style.width = "0%"
        i2.style.width = "100%"
        i2.style.left = "0%"
        i6.style.left = "100%"
        banner_mob2()
    },2000)
}
function banner_mob2(){
    setTimeout(function(){
        i2.style.width = "0%"
        i3.style.width = "100%"
        i3.style.left = "0%"
        i1.style.left = "100%"
        banner_mob3()
    },2000)
}
function banner_mob3(){
    setTimeout(function(){
        i3.style.width = "0%"
        i4.style.width = "100%"
        i4.style.left = "0%"
        i2.style.left = "100%"
        banner_mob4()
    },2000)
}
function banner_mob4(){
    setTimeout(function(){
        i4.style.width = "0%"
        i5.style.width = "100%"
        i5.style.left = "0%"
        i3.style.left = "100%"
        banner_mob5()
    },2000)
}
function banner_mob5(){
    setTimeout(function(){
        i5.style.width = "0%"
        i6.style.width = "100%"
        i6.style.left = "0%"
        i4.style.left = "100%"
        banner_mob6()
            },2000)
}
function banner_mob6(){
    setTimeout(function(){
        i6.style.width = "0%"
        i1.style.width = "100%"
        i1.style.left = "0%"
        i5.style.left = "100%"
        banner_mob1()
    },2000)
}


if(window.innerHeight > window.innerWidth)
{
    banner_mob1()
}
else{
    banner1()
    
}
