# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 13:01:02 2020

@author: OHyic
"""
#import selenium drivers
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

#import helper libraries
import time
import urllib.request
from urllib.parse import urlparse
import os
import requests
import io

import re

#custom patch libraries
import patch

import logging
from selenium.webdriver.remote.remote_connection import LOGGER as seleniumLogger

# Set the Selenium logging level to WARNING to suppress INFO and DEBUG messages
seleniumLogger.setLevel(logging.WARNING)

# The rest of your imports and code...





# Content
anime_file_path = r'prerelease\\anime_list.csv'
kanji_of_the_day_file_path = r'prerelease\\anime_list.csv'


# Specify the path to the Chrome browser executable first mode
chrome_binary_path_128 = "C:\\Program Files\\Google\\chrome\\Application\\chrome.exe"
chrome_user_data_dir_128 = "C:\\Users\\pc\\AppData\\Local\\Google\\Chrome for Testing\\User Data"

# Specify the path to the Chrome browser executable first mode
chrome_driver_path_127 = "C:\\Program Files\\Google\\chrome\\chromedriver\\chrome-win64\\127\\chromedriver.exe"
chrome_binary_path_127 = "C:\\Program Files\\Google\\chrome\\Application\\127\\chrome.exe"
chrome_user_data_dir_127 = "C:\\Users\\pc\\AppData\\Local\\Google\\Chrome for Testing\\User Data"

prompt = "Enter the path to the Chrome browser executable: "



class GoogleImageScraper():
    def __init__(self, image_path, search_key="cat", number_of_images=1, headless=True, min_resolution=(0, 0), max_resolution=(1920, 1080), max_missed=10):
        #check parameter types
        image_path = os.path.join(image_path, search_key)
        if (type(number_of_images)!=int):
            print("[Error] Number of images must be integer value.")
            return
        if not os.path.exists(image_path):
            print("[INFO] Image path not found. Creating a new folder.")
            os.makedirs(image_path)
            
        for i in range(1):
                                    
            try:
                        # Attempt to initialize using ChromeDriverManager


                            # Set Chrome options to use the specific Chrome binary
                            chrome_options = Options()
                            chrome_options.binary_location = chrome_binary_path_128
                            chrome_options.add_argument("--log-level=3")  # Reduce ChromeDriver logs
                            chrome_options.add_argument("--disable-logging")  # Suppress ChromeDriver logs

                            chrome_options.add_argument(f"--user-data-dir={chrome_user_data_dir_128}")
                            chrome_options.add_argument("--no-sandbox")  # Disable the sandbox
                            chrome_options.add_argument("--disable-dev-shm-usage")  # Disable shared memory usage

                            # Attempt to initialize using ChromeDriverManager
                            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
                            print("Chrome WebDriver initialized successfully with ChromeDriverManager.")

            except Exception as e:
                        # If there's an error, fall back to using the specified ChromeDriver path
                            try:
                            
                                chrome_options = Options()
                                chrome_options.binary_location = chrome_binary_path_127
                                chrome_options.add_argument(f"--user-data-dir={chrome_user_data_dir_127}")
                                chrome_options.add_argument("--log-level=3")  # Reduce ChromeDriver logs
                                chrome_options.add_argument("--disable-logging")  # Suppress ChromeDriver logs
                                chrome_options.add_argument("--no-sandbox")  # Disable the sandbox
                                chrome_options.add_argument("--disable-dev-shm-usage")  # Disable shared memory usage

                                print(f"Error initializing WebDriver with ChromeDriverManager:")
                                print("Trying to use the specified ChromeDriver path.")
                                driver = webdriver.Chrome(service=ChromeService(executable_path=chrome_driver_path_127), options=chrome_options)
                                print("Chrome WebDriver initialized successfully with specified ChromeDriver path.")

                            finally:        
                                
                                print("Error initializing WebDriver with ChromeDriverManager:")



        self.driver = driver
        self.search_key = search_key
        self.number_of_images = number_of_images
        self.image_path = image_path
        self.url = "https://www.google.com/search?q=%s&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947"%(search_key)
        self.headless=headless
        self.min_resolution = min_resolution
        self.max_resolution = max_resolution
        self.max_missed = max_missed
            # Wait for the page to load
        print("[INFO] Waiting for the page to load")






    def find_image_urls(self):
            print("[INFO] Gathering image links")
            self.driver.get(self.url)



            image_urls = []
            count = 0
            missed_count = 0

            while count<150 :
                try:
                    # Find all elements inside div with class 'jsslot'
                    jsslot_elements = self.driver.find_elements(By.CLASS_NAME, 'jsslot')

                    for element in jsslot_elements:
                        try:
                            # Click on the element to open the image in a larger view
                            self.driver.execute_script("arguments[0].click();", element)
                            time.sleep(1)

                            # Find all images in the expanded view
                            image_elements = self.driver.find_elements(By.XPATH, '//img[contains(@src, "http")]')
                            
                            for image in image_elements:
                                src_link = image.get_attribute("src")
                                if src_link and src_link.startswith("http") and not src_link.startswith("https://encrypted-tbn0.gstatic.com"):
                                    if src_link not in image_urls:  # Ensure no duplicates
                                        print(f"[INFO] Image {count + 1} found: {src_link}")
                                        image_urls.append(src_link)
                                        count += 1
                                        break

                            if count >= self.number_of_images:
                                break

                        except Exception as e:
                            print(f"[INFO] Failed to process element in 'jsslot': {e}")
                            missed_count += 1
                            continue

                    if count >= self.number_of_images:
                        break

                    # Scroll down to load more images
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)

                    # Try to click on the "Load more" button, if present
                    try:
                        load_more_button = self.driver.find_element(By.CLASS_NAME, "mye4qd")
                        self.driver.execute_script("arguments[0].click();", load_more_button)
                        time.sleep(2)
                    except NoSuchElementException:
                        print("[INFO] No more images to load")
                        break

                except Exception as e:
                    print(f"[ERROR] An unexpected error occurred: {e}")
                    

            self.driver.quit()
            print(f"[INFO] Google search ended with {count} images found.")
            return image_urls