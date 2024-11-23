/**
* Template Name: Impact
* Template URL: https://bootstrapmade.com/impact-bootstrap-business-website-template/
* Updated: Aug 07 2024 with Bootstrap v5.3.3
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/




(function() {
  "use strict";


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




 
const head = document.querySelector('head');

if (head) {
  // Set the innerHTML of the head
  head.innerHTML = `
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>Index - KanjiList.org Bootstrap Template</title>
  <meta name="description" content="">
  <meta name="keywords" content="">

  <!-- Favicons -->
  <link href="assets/img/favicon.png" rel="icon">
  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Fonts -->
  <link href="https://fonts.googleapis.com" rel="preconnect">
  <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
   <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
 <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&icon_names=language_japanese_kana" />

  <!-- Vendor CSS Files -->
  <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="assets/vendor/aos/aos.css" rel="stylesheet">
  <link href="assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
  <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">

  <!-- Main CSS File -->
  <link href="assets/css/main.css" rel="stylesheet">
 

  <!-- =======================================================
  * Template Name: KanjiList.org
  * Template URL: https://bootstrapmade.com/KanjiList.org-bootstrap-business-website-template/
  * Updated: Aug 07 2024 with Bootstrap v5.3.3
  * Author: BootstrapMade.com
  * License: https://bootstrapmade.com/license/
  ======================================================== --> 

  `;

  // DEBUGGING: Log changes to the console
  console.log("Modified menu:", head.innerHTML);
} else {
  console.error('The <ul> element was not found.');
}

  


  
  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  mobileNavToggleBtn.addEventListener('click', mobileNavToogle);

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });



  
  
  

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
    
    navmenu.addEventListener('click', function(e) {
      e.preventDefault();
      this.parentNode.classList.toggle('active');
      this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
      e.stopImmediatePropagation();
    });


  });

  /**
   * Preloader
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  scrollTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  /**
   * Initiate glightbox
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  window.addEventListener("load", initSwiper);

  /**
   * Initiate Pure Counter
   */
  new PureCounter();

  /**
   * Init isotope layout and filters
   */
  document.querySelectorAll('.isotope-layout').forEach(function(isotopeItem) {
    let layout = isotopeItem.getAttribute('data-layout') ?? 'masonry';
    let filter = isotopeItem.getAttribute('data-default-filter') ?? '*';
    let sort = isotopeItem.getAttribute('data-sort') ?? 'original-order';

    let initIsotope;
    imagesLoaded(isotopeItem.querySelector('.isotope-container'), function() {
      initIsotope = new Isotope(isotopeItem.querySelector('.isotope-container'), {
        itemSelector: '.isotope-item',
        layoutMode: layout,
        filter: filter,
        sortBy: sort
      });
    });

    isotopeItem.querySelectorAll('.isotope-filters li').forEach(function(filters) {
      filters.addEventListener('click', function() {
        isotopeItem.querySelector('.isotope-filters .filter-active').classList.remove('filter-active');
        this.classList.add('filter-active');
        initIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        if (typeof aosInit === 'function') {
          aosInit();
        }
      }, false);
    });

  });







  /**
   * Frequently Asked Questions Toggle
   */
  document.querySelectorAll('.faq-item h3, .faq-item .faq-toggle').forEach((faqItem) => {
    faqItem.addEventListener('click', () => {
      faqItem.parentNode.classList.toggle('faq-active');
    });
  });

  /**
   * Correct scrolling position upon page load for URLs containing hash links.
   */
  window.addEventListener('load', function(e) {
    if (window.location.hash) {
      if (document.querySelector(window.location.hash)) {
        setTimeout(() => {
          let section = document.querySelector(window.location.hash);
          let scrollMarginTop = getComputedStyle(section).scrollMarginTop;
          window.scrollTo({
            top: section.offsetTop - parseInt(scrollMarginTop),
            behavior: 'smooth'
          });
        }, 100);
      }
    }
  });

  /**
   * Navmenu Scrollspy
   */
  let navmenulinks = document.querySelectorAll('.navmenu a');

  function navmenuScrollspy() {
    navmenulinks.forEach(navmenulink => {
      if (!navmenulink.hash) return;
      let section = document.querySelector(navmenulink.hash);
      if (!section) return;
      let position = window.scrollY + 200;
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        document.querySelectorAll('.navmenu a.active').forEach(link => link.classList.remove('active'));
        navmenulink.classList.add('active');
      } else {
        navmenulink.classList.remove('active');
      }
    })
  }
  window.addEventListener('load', navmenuScrollspy);
  document.addEventListener('scroll', navmenuScrollspy);


  document.addEventListener("DOMContentLoaded", function() {
    // Target the <a> element with the class 'logo'
    const logoElement = document.querySelector('.logo');

    // Check if the element exists
    if (logoElement) {
      // Create a new <img> element for the logo
      const logoImage = document.createElement('img');
      logoImage.src = 'assets/img/logo.png';  // Set the source of the logo
      logoImage.alt = 'KanjiList.org Logo';  // Alt text for accessibility

      // Set the logo size dynamically in JS
      logoImage.style.width = '120%';   // Set the desired width in pixels
      logoImage.style.height = '120%';   // Maintain aspect ratio

      // Apply the filter to make the logo white (invert colors and adjust brightness)
      logoImage.style.filter = 'brightness(0) invert(1)';

      // Insert the image as the first child of the logo container
      logoElement.insertBefore(logoImage, logoElement.firstChild);

      // Optionally, you can also modify the sitename text (if needed)
      const sitenameElement = document.querySelector('.sitename');
      if (sitenameElement) {
        sitenameElement.textContent = '';  // Clear the original text
      }

    } else {
      console.error('Logo container element not found!');
    }
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
  





   /*==================================================================
    [ Show modal1 ]*/
    $('.js-show-modal1').on('click',function(e){
      e.preventDefault();
      $('.js-modal1').addClass('show-modal1');
  });

  $('.js-hide-modal1').on('click',function(){
      $('.js-modal1').removeClass('show-modal1');
  });

  document.addEventListener("DOMContentLoaded", function () {
    let kanjiData = [];
  
    // Fetch and parse the CSV file
    fetch('assets/kanji.csv')
      .then(response => response.text())
      .then(data => {
        // Parse the CSV file using '|' as the delimiter
        kanjiData = data.split('\n').slice(1).map(row => {
          const [
            id, kanji_symbol, url, freq_counter, jlpt_counter, school_counter,
            firstkanji, _, kun, on, meaning, table_data
          ] = row.split('|');  // Change ',' to '|'
  
          return {
            id: id?.trim(),
            kanji_symbol: kanji_symbol?.trim(),
            freq_counter: freq_counter?.trim(),
            jlpt_counter: jlpt_counter?.trim(),
            school_counter: school_counter?.trim(),
            firstkanji: firstkanji?.trim(),
            kun: kun?.trim(),
            on: on?.trim(),
            meaning: meaning?.trim(),
            table_data: table_data?.trim()
          };
        });
  
        console.log("CSV Data Loaded:"); // Debugging loaded data
      })
      .catch(err => console.error("Error loading CSV file:", err));
  
    // Open modal and populate data
    document.addEventListener("click", function (e) {
      if (e.target.classList.contains("kanji-link")) {
        e.preventDefault();
  
        const kanjiId = e.target.dataset.kanjiId;
        console.log("Kanji ID Clicked:", kanjiId); // Debugging clicked Kanji ID
  
        const kanjiRow = kanjiData.find(row => row.id === kanjiId);
        console.log("Kanji Data Found:", kanjiRow); // Debugging retrieved Kanji data
  
        if (kanjiRow) {

          

            console.log("Kanji Symbol:", kanjiRow.kanji_symbol);

          document.getElementById("kanjitop").textContent = kanjiRow.kanji_symbol;
          document.getElementById("kanjiMeaning").textContent = kanjiRow.meaning;
          document.getElementById("kanjiKun").textContent = kanjiRow.kun;
          document.getElementById("kanjiOn").textContent = kanjiRow.on;
  
         // Render the table data from 'table_data'
      
          const tableContent = JSON.parse(kanjiRow.table_data.replace(/'/g, '"')).map(row => {
            return `
              <tr>
                <td>${row.Word}</td>
                <td>${row.Reading}</td>
                <td>${row.Meaning}</td>
              </tr>
            `;
          }).join('');

          // Add the table headers at the top
          const tableHeader = `
            <tr>
              <th><strong>Word</strong></th>
              <th><strong>Reading</strong></th>
              <th><strong>Meaning</strong></th>
            </tr>
          `;

          // Insert the table content into the modal's table, including the headers
          document.getElementById("kanjiTable").innerHTML = tableHeader + tableContent;

  
          // Show modal
          document.querySelector(".wrap-modal1").classList.add("show-modal1");
        } else {
          console.error("Kanji ID not found in CSV data:", kanjiId);
        }
      }
    });
  
    // Close modal on button or overlay click
    document.querySelectorAll(".js-hide-modal1").forEach(button => {
      button.addEventListener("click", function () {
        console.log("Closing modal"); // Debugging modal close event
        document.querySelector(".wrap-modal1").classList.remove("show-modal1");
        document.getElementById("kanjiTitle").textContent = '';
        document.getElementById("kanjiMeaning").textContent = '';
        document.getElementById("kanjiKun").textContent = '';
        document.getElementById("kanjiOn").textContent = '';
        document.getElementById("kanjiTable").innerHTML = '';
      });
    });
  });
  
  
  
  
  

})();

// Array placeholders for Kanji and Vocabulary
let kanjis = [];
const vocab = ['こんにちは', 'ありがとう', 'さようなら', 'すみません', 'はい'];

let currentKanjiIndex = 0;
let currentVocabIndex = 0;

// Load Kanji from CSV
function loadKanjiFromCSV() {
    fetch('assets/kanji.csv')
        .then(response => response.text())
        .then(data => {
            parseCSV(data);
            if (kanjis.length > 0) {
                showKanji(); // Automatically display the Kanji section once loaded
            } else {
                alert('No Kanji data loaded. Please check the CSV file.');
            }
        })
        .catch(error => console.error('Error loading Kanji CSV:', error));
}

// Parse CSV and extract the "kanji_symbol" column
function parseCSV(data) {
    const rows = data.split('\n'); // Split into rows
    const headers = rows.shift().split('|').map(header => header.trim()); // Get headers and trim whitespace
    const kanjiSymbolIndex = headers.indexOf('kanji_symbol'); // Find the index of "kanji_symbol"

    if (kanjiSymbolIndex === -1) {
        console.error('The column "kanji_symbol" was not found in the CSV file.');
        return;
    }

    // Extract Kanji symbols
    kanjis = rows
        .map(row => row.split('|')[kanjiSymbolIndex]?.trim()) // Get the value in the "kanji_symbol" column
        .filter(kanji => kanji); // Filter out empty rows or values
}

// Show Kanji section
function showKanji() {
    document.getElementById('kanji-section').style.display = 'block';
    document.getElementById('vocab-section').style.display = 'none';
    updateKanjiDisplay();
}

// Show Vocabulary section
function showVocabulary() {
    document.getElementById('kanji-section').style.display = 'none';
    document.getElementById('vocab-section').style.display = 'block';
    updateVocabDisplay();
}

// Update Kanji display
function updateKanjiDisplay() {
    if (kanjis.length > 0) {
        document.getElementById('kanji-char').innerText = kanjis[currentKanjiIndex];
    } else {
        document.getElementById('kanji-char').innerText = 'No Kanji available';
    }
}

// Navigate to the next Kanji
function nextKanji() {
    if (kanjis.length > 0) {
        currentKanjiIndex = (currentKanjiIndex + 1) % kanjis.length;
        updateKanjiDisplay();
    }
}

// Navigate to the previous Kanji
function prevKanji() {
    if (kanjis.length > 0) {
        currentKanjiIndex = (currentKanjiIndex - 1 + kanjis.length) % kanjis.length;
        updateKanjiDisplay();
    }
}

// Show information about the current Kanji
function showKanjiInfo() {
    if (kanjis.length > 0) {
        const kanji = kanjis[currentKanjiIndex];
        alert(`Information about ${kanji}: Example info could go here.`);
    }
}

// Update Vocabulary display
function updateVocabDisplay() {
    document.getElementById('vocab-word').innerText = vocab[currentVocabIndex];
}

// Navigate to the next Vocabulary word
function nextVocab() {
    currentVocabIndex = (currentVocabIndex + 1) % vocab.length;
    updateVocabDisplay();
}

// Navigate to the previous Vocabulary word
function prevVocab() {
    currentVocabIndex = (currentVocabIndex - 1 + vocab.length) % vocab.length;
    updateVocabDisplay();
}

// Show information about the current Vocabulary word
function showVocabInfo() {
    const word = vocab[currentVocabIndex];
    alert(`Information about ${word}: Example info could go here.`);
}

// Update difficulty (placeholder for functionality)
function updateDifficulty() {
    const difficulty = document.getElementById('difficulty').value;
    alert(`Difficulty set to: ${difficulty}`);
}

// Load Kanji on page load
document.addEventListener('DOMContentLoaded', loadKanjiFromCSV);
