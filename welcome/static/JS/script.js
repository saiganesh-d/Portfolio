/*$(document).ready(function(){
    $(window).scroll(function(){
        if(this.scrollY > 10){
            $('.navbar').addClass("sticky");
        }else{
            $('.navbar').removeClass("sticky");
        }
    })
})





/*function myFunction() {
    var str = "Github repo";
    var result = str.link("https://www.w3schools.com");
    
    
    document.getElementById("demo").innerHTML = result;
  }*/

/*var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-50px";
  }
  prevScrollpos = currentScrollPos;
}*/

/*$(function(){
    var scroll = $(document).scrollTop();
    var navHeight = $('.navbar').outerHeight();

    $(window).scroll(function(){
        var scrolled=$(document).scrollTop();

        if(scrolled > navHeight){
            $('.navbar').addClass('animate');

        }else{
            $('navbar').removeClass('animate;');
        }

        if(scrolled > scroll){
            $('.navbar').removeClasss('sticky');
        }else{
            $('.navbar').addClass('sticky');
        }
        scroll = $(document).scrollTop();
        });
    });*/

    var scroll1 = window.pageYOffset;
    window.onscroll=function(){
        var scroll2 = window.pageYOffset;
        if(scroll1 > scroll2){
            document.querySelector('.navbar').style.top = "0";
        }else{
            document.querySelector('.navbar').style.top = "-100px";

        }
        scroll1=scroll2;
        }
    

