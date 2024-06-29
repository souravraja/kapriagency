let SearchForm=document.querySelector('.search-form');
let shoppingcart=document.querySelector('.shopping-card')
console.log('log is ',SearchForm)
document.querySelector('#search-btn').onclick=()=>{
    SearchForm.classList.toggle('active');
    shoppingcart.classList.remove('active')
    navbar.classList.remove('active')
}
document.querySelector('#cart-btn').onclick=()=>{
    SearchForm.classList.remove('active')
    shoppingcart.classList.toggle('active');
    navbar.classList.remove('active')
}


let navbar=document.querySelector('.navbar')
document.querySelector('#menu-btn').onclick=()=>{
    SearchForm.classList.remove('active')
    shoppingcart.classList.remove('active')
     navbar.classList.toggle('active')
}

window.onscroll=()=>{
    SearchForm.classList.remove('active')
    shoppingcart.classList.remove('active')
    navbar.classList.remove('active')
}


var swiper = new Swiper(".product-slider", {
    loop:true,
    spaceBetween: 20,

    autoplay:{
        delay:1500,
        disableOnInteraction:false,
        },

    breakpoints: {
      0: {
        slidesPerView: 1,
       
      },
      768: {
        slidesPerView: 2,
        
      },
      1024: {
        slidesPerView: 3,
        
      },
    },
  });