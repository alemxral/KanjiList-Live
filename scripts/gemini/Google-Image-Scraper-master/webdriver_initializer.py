# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 13:01:02 2020

@author: OHyic
"""

# Import selenium drivers and utilities
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import logging
from selenium.webdriver.remote.remote_connection import LOGGER as seleniumLogger
import os

# Set the Selenium logging level to WARNING to suppress INFO and DEBUG messages
seleniumLogger.setLevel(logging.WARNING)

# Define paths for Chrome browser executable and user data
chrome_binary_path_128 = "C:\\Program Files\\Google\\chrome\\Application\\chrome.exe"
chrome_user_data_dir_128 = "C:\\Users\\pc\\AppData\\Local\\Google\\Chrome for Testing\\User Data"

chrome_driver_path_127 = "C:\\Program Files\\Google\\chrome\\chromedriver\\chrome-win64\\127\\chromedriver.exe"
chrome_binary_path_127 = "C:\\Program Files\\Google\\chrome\\Application\\127\\chrome.exe"
chrome_user_data_dir_127 = "C:\\Users\\pc\\AppData\\Local\\Google\\Chrome for Testing\\User Data"


def initialize_webdriver(search_key="cat", image_path="./images", number_of_images=1, headless=True, min_resolution=(0, 0), max_resolution=(1920, 1080), max_missed=10):
    """
    Initialize the Chrome WebDriver with specified options and parameters.

    :param search_key: The search term for Google Images.
    :param image_path: The path where images will be saved.
    :param number_of_images: Number of images to download.
    :param headless: Boolean indicating whether to run Chrome in headless mode.
    :param min_resolution: Minimum resolution of images to download.
    :param max_resolution: Maximum resolution of images to download.
    :param max_missed: Maximum number of missed images before stopping.
    :return: Initialized WebDriver instance and other parameters.
    """
    
    # Prepare the image path
    image_path = os.path.join(image_path, search_key)
    if not os.path.exists(image_path):
        print("[INFO] Image path not found. Creating a new folder.")
        os.makedirs(image_path)
    
    try:
        # Set Chrome options to use the specific Chrome binary
        chrome_options = Options()
        chrome_options.binary_location = chrome_binary_path_128
        chrome_options.add_argument("--log-level=3")  # Reduce ChromeDriver logs
        chrome_options.add_argument("--disable-logging")  # Suppress ChromeDriver logs
        chrome_options.add_argument(f"--user-data-dir={chrome_user_data_dir_128}")
        chrome_options.add_argument("--no-sandbox")  # Disable the sandbox
        chrome_options.add_argument("--disable-dev-shm-usage")  # Disable shared memory usage
        chrome_options.headless = headless  # Enable headless mode if specified

        # Attempt to initialize using ChromeDriverManager
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        print("Chrome WebDriver initialized successfully with ChromeDriverManager.")

    except Exception as e:
        print(f"Error initializing WebDriver with ChromeDriverManager: {e}")
        try:
            # If there's an error, fall back to using the specified ChromeDriver path
            chrome_options = Options()
            chrome_options.binary_location = chrome_binary_path_127
            chrome_options.add_argument(f"--user-data-dir={chrome_user_data_dir_127}")
            chrome_options.add_argument("--log-level=3")  # Reduce ChromeDriver logs
            chrome_options.add_argument("--disable-logging")  # Suppress ChromeDriver logs
            chrome_options.add_argument("--no-sandbox")  # Disable the sandbox
            chrome_options.add_argument("--disable-dev-shm-usage")  # Disable shared memory usage
            chrome_options.headless = headless  # Enable headless mode if specified

            driver = webdriver.Chrome(service=ChromeService(executable_path=chrome_driver_path_127), options=chrome_options)
            print("Chrome WebDriver initialized successfully with specified ChromeDriver path.")
        except Exception as final_error:
            print(f"Error initializing WebDriver with specified ChromeDriver path: {final_error}")
            raise

    # Set the URL for Google Images search
    url = "https://www.google.com/search?q=%s&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947" % search_key

    # Return the WebDriver and other necessary parameters
    return driver, search_key, image_path, number_of_images, url, headless, min_resolution, max_resolution, max_missed

