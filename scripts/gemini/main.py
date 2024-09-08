from selenium import webdriver
import logging
import warnings
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from input_finder import find_and_send_keys
from text_extractor import extract_text_from_response_container
from datetime import datetime
from settings import *

# Get the current time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Current time: {current_time}")

# Reduce Python logging output
logging.basicConfig(level=logging.ERROR)  # Set the logging level to ERROR

# Suppress specific warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)





try:
# Attempt to initialize using ChromeDriverManager


    # Set Chrome options to use the specific Chrome binary
    chrome_options = Options()
    chrome_options.binary_location = chrome_binary_path_128
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
        chrome_options.add_argument("--no-sandbox")  # Disable the sandbox
        chrome_options.add_argument("--disable-dev-shm-usage")  # Disable shared memory usage

        print(f"Error initializing WebDriver with ChromeDriverManager:")
        print("Trying to use the specified ChromeDriver path.")
        driver = webdriver.Chrome(service=ChromeService(executable_path=chrome_driver_path_127), options=chrome_options)
        print("Chrome WebDriver initialized successfully with specified ChromeDriver path.")

    finally:        
        
        print("Error initializing WebDriver with ChromeDriverManager:")

   

# Navigate to the desired URL
driver.get("https://gemini.google.com/app")
print("Navigated to the specified URL.")

# Wait for the page to load
time.sleep(30)  # Replace this with WebDriverWait for efficiency

# Attempt to find the correct input element and send keys
try:
    successful_element = find_and_send_keys(driver, prompt)
    print(f"Successfully sent keys to element: {successful_element}")
except Exception as e:
    print(f"Failed to send keys: {e}")

# Optionally wait for the response to be generated
time.sleep(5)  # Adjust as necessary

# Extract and print the chat text
try:
    chat_text = extract_text_from_response_container(driver)
    print(f"Extracted chat text:")
except Exception as e:
    print(f"Failed to extract chat text: {e}")

# Keep the browser open for a while to observe
time.sleep(10000)
