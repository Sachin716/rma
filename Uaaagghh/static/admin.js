var xbook = 0;
var xapp = 0;
const bok = document.querySelector(".Book-items");
const app = document.querySelector(".app-items");
const a = document.querySelector(".Appoint");
function openBook(){
    if (xbook == 0){ 
    a.style.top = "121%";
    app.style.top = "126%"
    bok.style.height = "100%";
    bok.style.overflowY = "scroll";
    xbook = 1;
    }
    else{ 
    a.style.top = "21%";
    bok.style.height = "0%";
    app.style.top = "26%"
    bok.style.overflowY = "hidden";
    xbook = 0;
    }

}

function openApp(){
    if (xapp == 0){ 
        app.style.height = "100%";
        app.style.overflowY = "scroll";
        xapp = 1;
        }
        else{ 
        app.style.height = "0%";
        app.style.overflowY = "hidden";
        xapp = 0;
        }
}