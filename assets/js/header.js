// header.js

export const headerHTML = `
  <ul>
      <li><a href="#hero" class="active">Home<br></a></li>
      <li><a href="#about">About</a></li>
      <li><a href="#services">Services</a></li>
      <li><a href="#portfolio">Portfolio</a></li>
      <li><a href="#team">Team</a></li>
      <li><a href="blog.html">Blog</a></li>
      <li class="dropdown 1"><a href="#"><span>Kanji Lists</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
        <ul>
          <li><a href="#">By Frequency Order</a></li>
          <li><a href="#">By School Grade Order</a></li>
          <li><a href="#">By JLPT Order</a></li>
        </ul>
      </li>
      <li class="dropdown 2"><a href="#"><span>Dropdown</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
        <ul>
          <li><a href="#">Dropdown 1</a></li>
          <li class="dropdown"><a href="#"><span>Deep Dropdown</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
            <ul>
              <li><a href="#">Deep Dropdown 1</a></li>
              <li><a href="#">Deep Dropdown 2</a></li>
              <li><a href="#">Deep Dropdown 3</a></li>
              <li><a href="#">Deep Dropdown 4</a></li>
              <li><a href="#">Deep Dropdown 5</a></li>
            </ul>
          </li>
          <li><a href="#">Dropdown 2</a></li>
          <li><a href="#">Dropdown 3</a></li>
          <li><a href="#">Dropdown 4</a></li>
        </ul>
      </li>
      <li><a href="#contact">Contact</a></li>
    </ul>
    <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
`;
