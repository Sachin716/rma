const sheight = document.querySelector("html").scrollHeight;
const height = window.innerHeight;
const width = window.innerWidth;
if(window.innerWidth > 1090){
    document.addEventListener("DOMContentLoaded" , () =>{
document.querySelector(".seperator").style.height = (window.innerHeight*1.2) + "px";
let sheight2 = document.querySelector("body").scrollHeight;
document.querySelector(".footer").style.top = (sheight2/height)*100 + "%" ;
document.querySelector("#contact").style.top = ((sheight2/height)*100)-15 + "%" ;
document.querySelector(".award").style.bottom = (100 - ((sheight2/height)*100) +70) + "%";
document.querySelector(".rev_cont").style.bottom = (100 - ((sheight2/height)*100) +20) + "%";
document.querySelector(".sers2").style.bottom = (100 - ((sheight2/height)*100) +55) + "%";
})
}

else{
document.addEventListener("DOMContentLoaded" , () =>{
    document.querySelector(".seperator").style.height = (window.innerHeight) + "px";
    let sheight2 = (document.querySelector("body").scrollHeight);
    document.querySelector(".footer").style.top =  ((sheight2/height))*100 + "%" ;
    document.querySelector("#contact").style.top = (((sheight2/height))*100-7.5) + "%" ;
    document.querySelector(".award").style.bottom = (100 - ((sheight2/height)*100) +70) + "%";
    document.querySelector(".rev_cont").style.bottom = (100 - ((sheight2/height)*100) +20) + "%";
    document.querySelector(".sers2").style.bottom = (100 - ((sheight2/height)*100) +55) + "%";
})
    

}