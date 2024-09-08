# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 13:01:02 2020

@author: OHyic
"""

# Import necessary libraries
import os
import time
import requests
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# Import custom WebDriver initializer
from webdriver_initializer import initialize_webdriver

class GoogleImageScraper:
    def __init__(self, search_key="cat", image_path="./images", number_of_images=10, headless=True):
        """Initialize the scraper with search parameters."""
        print("[INFO] Initializing WebDriver and setting up search parameters...")
        self.driver, self.search_key, self.image_path, self.number_of_images, self.url = self._initialize_scraper(
            search_key=search_key, 
            image_path=image_path, 
            number_of_images=number_of_images, 
            headless=headless
        )
        print(f"[INFO] WebDriver initialized successfully.\n[INFO] Searching for: '{self.search_key}'\n[INFO] Images will be saved to: '{self.image_path}'")

    def _initialize_scraper(self, search_key, image_path, number_of_images, headless):
        """Helper function to initialize WebDriver and set URL."""
        print("[INFO] Setting up the WebDriver...")
        driver = initialize_webdriver()[0]
        image_path = os.path.join(image_path, search_key)
        if not os.path.exists(image_path):
            print(f"[INFO] Image path '{image_path}' not found. Creating a new folder...")
            os.makedirs(image_path)
        url = f"https://www.google.com/search?q={search_key}&source=lnms&tbm=isch"
        return driver, search_key, image_path, number_of_images, url

    def fetch_image_urls(self):
        """Fetch image URLs from the Google Images search results."""
        print("[INFO] Fetching image URLs...")
        self.driver.get(self.url)
        time.sleep(5)  # Wait for the page to load

        # Scroll down to load more images
        scroll_pause_time = 2
        for _ in range(10):  # Adjust number of scrolls to load more images
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)

        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        actual_images = []

        # Extract image URLs
        print("[INFO] Inside FOR loop for image tags with 'id' attribute.")
        for tag in soup.findAll('img'):
            if tag.get('id'):  # Check if the image tag has an 'id' attribute
                img_url = tag.get('src', tag.get('dfr-src'))  # Try to get 'src', fallback to 'dfr-src'
                
                if img_url and not img_url.lower().endswith('.png'):  # Skip PNG files
                    if not img_url.startswith('https://encrypted-tbn0.gstatic.com'):  # Skip encrypted URLs
                        try:
                            # Check if the image is large enough
                            response = requests.get(img_url, stream=True)
                            img = Image.open(BytesIO(response.content))
                            width, height = img.size
                            
                            if width >= 200 and height >= 200:  # Skip small images (e.g., logos, thumbnails)
                                actual_images.append(img_url)
                            else:
                                print(f"[INFO] Skipping small image: {img_url}")
                        except Exception as e:
                            print(f"[WARNING] Could not load or process image URL {img_url}.")
                            print(f"[WARNING] {e}")
                    else:
                        print(f"[INFO] Skipping encrypted image URL: {img_url}")
                elif img_url and img_url.lower().endswith('.png'):
                    print(f"[INFO] Skipping PNG image: {img_url}")
                else:
                    print("[WARNING] Image tag does not contain 'src' or 'dfr-src'.")

        print(f"[INFO] Found {len(actual_images)} suitable images (excluding PNGs and small images).")

        # Save the URLs to a text file
        url_txt_path = os.path.join(self.image_path, "image_urls.txt")
        with open(url_txt_path, 'w') as url_file:
            for img_url in actual_images:
                url_file.write(img_url + "\n")
        print(f"[INFO] Image URLs saved to {url_txt_path}")

        return actual_images[:self.number_of_images]

    def download_images(self):
        """Download images from the fetched URLs."""
        print("[INFO] Starting image download process...")
        images = self.fetch_image_urls()

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        for i, img_url in enumerate(images):
            try:
                print(f"[INFO] Downloading image {i + 1} from {img_url}...")
                req = Request(img_url, headers=headers)
                raw_img = urlopen(req).read()

                img_path = os.path.join(self.image_path, f"img_{i + 1}.jpg")
                with open(img_path, 'wb') as f:
                    f.write(raw_img)

                print(f"[INFO] Image {i + 1} downloaded successfully: {img_path}")
            except Exception as e:
                print(f"[ERROR] Could not load image {i + 1} from {img_url}.")
                print(f"[ERROR] {e}")

        print("[INFO] Image download process completed. Closing the WebDriver...")
        # Close the driver
        self.driver.quit()

# Example usage
if __name__ == "__main__":
    search_key = "cats"
    image_path = r"C:\Users\pc\pyprojects\KanjiList\kanjilist-live\scripts\gemini\Google-Image-Scraper-master\photos"
    scraper = GoogleImageScraper(image_path=image_path, search_key=search_key, number_of_images=10, headless=True)
    scraper.download_images()
