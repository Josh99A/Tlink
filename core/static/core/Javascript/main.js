 /**
   * Easy selector helper function
   */
 const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }



// Generic category slider
const category_swiper = (selector) => {
    var swipers = select(selector, true)

    
    var swipers = select(selector, true)

    swipers.forEach(function(swiper){
        const Myswiper = new Swiper(swiper, {
          loop: true,
          pagination: {
              el: '.swiper-pagination',
              clickable: 'true'
          },
          navigation : {
              nextEl: '.swiper-button-next',
              prevEl: '.swiper-button-prev',
      
          },
          
          autoplay:{
            delay: 5000,
          },
      
          slidesPerView: 'auto'
      }
    )

})
}

category_swiper('.category-intro')

// Generic swiper function
const swiper_func = (selector) => {

    var swipers = select(selector, true)

    swipers.forEach(function(swiper){
        const Myswiper = new Swiper(swiper, {
          loop: true,
      navigation : {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
  
      },
      slidesPerView: 'auto',
      autoplay:{
          delay: 5000,
      },
      autoplayDisableOnInteraction :true,
      pauseOnMouseEnter: true,
  },
  )

})}

swiper_func('.top-deals')
swiper_func('.ps-swiper')

/**
   * Back to top button
   */
let backtotop = select('.back-to-top')
if (backtotop) {
  const toggleBacktotop = () => {
    if (window.scrollY > 100) {
      backtotop.classList.add('active')

    } else {
        backtotop.classList.remove('active')
       
    }
  }
  window.addEventListener('load', toggleBacktotop)
  onscroll(document, toggleBacktotop)
}


document.addEventListener('DOMContentLoaded', () => {
     // Functions to open and close a modal
      function openModal($el) {
         $el.classList.add('is-active');
         }

      function closeModal($el) {
         $el.classList.remove('is-active');
         
        }
         
       function closeAllModals() { (document.querySelectorAll('.modal') || []).forEach(($modal) => {
         closeModal($modal);
         }); }
         
         // Add a click event on buttons to open a specific modal 
         
        (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
            const modal = $trigger.dataset.target;
            const $target = document.getElementById(modal);
            
            $trigger.addEventListener('click', () => { openModal($target);
             });
            });
        // Add a click event on various child elements to close the parent modal 
        
        (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
            const $target = $close.closest('.modal');

            $close.addEventListener('click', () => { 
                closeModal($target);
             });
         }); 
         
         // Add a keyboard event to close all modals
        document.addEventListener('keydown', (event) => {
            if (event.code === 'Escape') {
                closeAllModals();
             } });
            
            });