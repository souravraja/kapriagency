let searchBtn=document.querySelector('.searchBtn');
let closeBtn=document.querySelector('.closeBtn');
let searchBox=document.querySelector('searchBox');
let menuToggle=document.querySelector('.menuToggle');
let header=document.querySelector('header');
let navigation=document.querySelector('.navigation');

searchBtn.onclick=function(){
    searchBox.classList.add('active');
    closeBtn.classList.add('active');
    searchBtn.classList.add('active');
    menuToggle.classList.add('hide');
    header.classList.remove('open');
}
closeBtn.onclick=function(){
    searchBox.classList.remove('active');
    closeBtn.classList.remove('active');
    searchBtn.classList.aremove('active');
    menuToggle.classList.remove('hide');

}
menuToggle.onclick=function(){
    header.classList.toggle('open');
    searchBox.classList.remove('active');
    closeBtn.classList.remove('active');
    searchBtn.classList.aremove('active');
}