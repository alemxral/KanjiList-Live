from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from input_finder import find_and_send_keys
from text_extractor import extract_text_from_response_container

# Specify the path to the Chrome browser executable
chrome_binary_path = "C:\\Users\\pc\\Documents\\chromedriver\\chrome-win64\\chrome-win64\\chrome.exe"
chrome_user_data_dir = "C:\\Users\\pc\\AppData\\Local\\Google\\Chrome for Testing\\User Data"

# Set Chrome options to use the specific Chrome binary
chrome_options = Options()
chrome_options.binary_location = chrome_binary_path
chrome_options.add_argument(f"--user-data-dir={chrome_user_data_dir}")
chrome_options.add_argument("--no-sandbox")  # Disable the sandbox
chrome_options.add_argument("--disable-dev-shm-usage")  # Disable shared memory usage

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# Navigate to the desired URL
driver.get("https://gemini.google.com/app")

# Wait for the page to load
time.sleep(30)  # Replace this with WebDriverWait for efficiency

# Attempt to find the correct input element and send keys
try:
    successful_element = find_and_send_keys(driver, "tell me a story in Japanese")
    print(f"Successfully sent keys to element: {successful_element}")
except Exception as e:
    print(f"Failed to send keys: {e}")

# Optionally wait for the response to be generated
time.sleep(5)  # Adjust as necessary

# Extract and print the chat text
try:
    chat_text = extract_text_from_response_container(driver)
    print(f"Extracted chat text:\n{chat_text}")
except Exception as e:
    print(f"Failed to extract chat text: {e}")

# Keep the browser open for a while to observe
time.sleep(10000)
