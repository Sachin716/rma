var x = document.querySelector("body");
var y = x.scrollTop;
        function myfunc(){

            if(window.innerWidth < 1090){
            if(x.scrollTop == 0){
                document.querySelector('.NavBar').style.backgroundColor = '#00000066';
                document.querySelector('.NavBar').style.top = '2%';
                document.querySelector('.hider').style.backgroundColor = "transparent";
                
            }
            else if(x.scrollTop > y){
                document.querySelector('.NavBar').style.height = '5%';
                document.querySelector('.NavBar').style.top = '0%';
 
                document.querySelector('.logo').style.left = "90%";
                document.querySelector('.bar').style.left = "3%";
                document.querySelector('.text').style.left = "-25%";
                document.querySelector('.hider').style.width = "5%";
                document.querySelector('.NavBar').style.backgroundColor = 'black';
                document.querySelector('.hider').style.backgroundColor = "black";
                y = x.scrollTop;

            }
            else if(x.scrollTop < y){
                document.querySelector('.NavBar').style.top = '0%';
                document.querySelector('.NavBar').style.height = '10%';
                document.querySelector('.logo').style.left = "3%";
                document.querySelector('.text').style.left = "14%";
                document.querySelector('.hider').style.width = "7%";
                document.querySelector('.bar').style.left = "-60%";
                
                
               
                y = x.scrollTop;

            }
        }
            else{
            if(x.scrollTop == 0){
                document.querySelector('.NavBar').style.backgroundColor = '#00000066';
                document.querySelector('.NavBar').style.top = '2%';
                document.querySelector('.hider').style.backgroundColor = "transparent";
                
            }
            else if(x.scrollTop > y){
                document.querySelector('.NavBar').style.height = '5%';
                document.querySelector('.NavBar').style.top = '0%';
 
                document.querySelector('.logo').style.left = "90%";
                document.querySelector('.bar').style.left = "3%";
                document.querySelector('.text').style.left = "-25%";
                document.querySelector('.hider').style.width = "5%";
                document.querySelector('.NavBar').style.backgroundColor = 'black';
                document.querySelector('.hider').style.backgroundColor = "black";
                y = x.scrollTop;

            }
            else if(x.scrollTop < y){
                document.querySelector('.NavBar').style.top = '0%';
                document.querySelector('.NavBar').style.height = '10%';
                document.querySelector('.logo').style.left = "3%";
                document.querySelector('.text').style.left = "7%";
                document.querySelector('.hider').style.width = "7%";
                document.querySelector('.bar').style.left = "-60%";
                
                
               
                y = x.scrollTop;

            }
            
        }
        }
    