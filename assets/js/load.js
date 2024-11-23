/**
* Template Name: Impact
* Template URL: https://bootstrapmade.com/impact-bootstrap-business-website-template/
* Updated: Aug 07 2024 with Bootstrap v5.3.3
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/




(function() {
  "use strict";



   /**
   * Preloader
   */
   const preloader = document.querySelector('#preloader');
   if (preloader) {
     window.addEventListener('load', () => {
       preloader.remove();
     });
   }


const navmenu = document.querySelector('.navmenu');

document.addEventListener("DOMContentLoaded", function() {
  // Footer HTML content
  const footerHTML = `
    <footer id="footer" class="footer accent-background">
      <div class="container footer-top">
        <div class="row gy-4">
          <div class="col-lg-5 col-md-12 footer-about">
            <a href="index.html" class="logo d-flex align-items-center">
              <span class="sitename">KanjiList.org</span>
            </a>
            <p>KanjiList.org is dedicated to helping learners master Japanese with curated Kanji and vocabulary resources, interactive flashcards, and efficient learning tools.</p>
            <div class="social-links d-flex mt-4">
              <a href="https://twitter.com/kanjilist" target="_blank"><i class="bi bi-twitter"></i></a>
              <a href="https://facebook.com/kanjilist" target="_blank"><i class="bi bi-facebook"></i></a>
              <a href="https://instagram.com/kanjilist" target="_blank"><i class="bi bi-instagram"></i></a>
              <a href="https://linkedin.com/company/kanjilist" target="_blank"><i class="bi bi-linkedin"></i></a>
            </div>
          </div>

          <div class="col-lg-2 col-6 footer-links">
            <h4>Useful Links</h4>
            <ul>
              <li><a href="index.html">Home</a></li>
              <li><a href="privacy.html">Privacy policy</a></li>
              <li><a href="contact.html">Contact</a></li>
            </ul>
          </div>

          <div class="col-lg-2 col-6 footer-links">
            <h4>Our Resources</h4>
            <ul>
              <li><a href="kanji-list-by-freq.html">By Frequency Order</a></li>
          <li><a href="kanji-list-by-grade.html">By School Grade Order</a></li>
          <li><a href="kanji-list-by-jlpt-level.html">By JLPT Order</a></li>
                    <li><a href="100_words.html">Top Frequent 100 Words</a></li>
          <li><a href="1K_words.html">Top Frequent 1000 Words</a></li>
          <li><a href="2K_words.html">Top Frequent 2000 Words </a></li>
          <li><a href="5K_words.html">Top Frequent 5000 Words </a></li>
          <li><a href="10K_words.html">Top Frequent 10000 Words </a></li>
          
          <li><a href="nouns_list.html">Top Frequent Nouns </a></li>
          <li><a href="adjectives_list.html">Top Frequent Adjectives</a></li>
          <li><a href="verbs_list.html">Top Frequent Verbs</a></li>
          <li><a href="practice.html">Practice Module</a></li>

            </ul>
          </div>

          <div class="col-lg-3 col-md-12 footer-contact text-center text-md-start">
            <h4>Contact Us</h4>
            <p><strong>Email:</strong> <span>info@kanjilist.org</span></p>
          </div>
        </div>
      </div>

      <div class="container copyright text-center mt-4">
        <p>© <span>Copyright</span> <strong class="px-1 sitename">KanjiList.org</strong> <span>All Rights Reserved</span></p>
        <div class="credits">
          Designed by <a href="https://bootstrapmade.com/">BootstrapMade</a>
        </div>
      </div>
    </footer>
  `;

  // Insert footer at the end of the body
  document.body.insertAdjacentHTML("beforeend", footerHTML);
});


if (navmenu) {
  // Set the innerHTML of the navmenu
  navmenu.innerHTML = `
    <ul>
      <li><a href="index.html" class="active">Home<br></a></li>
      <li class="dropdown 1"><a><span>Kanji Lists</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
        <ul>
          <li><a href="kanji-list-by-freq.html">By Frequency Order</a></li>
          <li><a href="kanji-list-by-grade.html">By School Grade Order</a></li>
          <li><a href="kanji-list-by-jlpt-level.html">By JLPT Order</a></li>
        </ul>
      </li>
            <li class="dropdown 1"><a><span>Vocabulary Lists</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
        <ul>
          <li><a href="100_words.html">Top Frequent 100 Words</a></li>
          <li><a href="1K_words.html">Top Frequent 1000 Words</a></li>
          <li><a href="2K_words.html">Top Frequent 2000 Words </a></li>
          <li><a href="5K_words.html">Top Frequent 5000 Words </a></li>
          <li><a href="10K_words.html">Top Frequent 10000 Words </a></li>
          
          <li><a href="nouns_list.html">Top Frequent Nouns </a></li>
          <li><a href="adjectives_list.html">Top Frequent Adjectives</a></li>
          <li><a href="verbs_list.html">Top Frequent Verbs</a></li>


        </ul>
      </li>
       <li><a href="practice.html">Practice Module</a></li>
        <li><a href="blog.html">Blog</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul>
    <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
  `;

  // DEBUGGING: Log changes to the console
  console.log("Modified menu:", navmenu.innerHTML);
} else {
  console.error('The <ul> element was not found.');
}


  

  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  mobileNavToggleBtn.addEventListener('click', mobileNavToogle);

  
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });




  

  









  document.addEventListener("DOMContentLoaded", function() {
    // Target the <h1> element with the class 'sitename'
    const sitenameElement = document.querySelector('.sitename');
    
    // Check if the element exists
    if (sitenameElement) {
      // Change the content of the <h1>
      sitenameElement.textContent = "KanjiList.org";  // Replace with your desired text
    } else {
      console.error('Sitename element not found!');
    }
  });
  





  
  
  
  
  
  

})();


