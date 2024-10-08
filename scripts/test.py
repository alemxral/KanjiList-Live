from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

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

# Use an XPath expression to find the container based on a partial match of the class name
container_xpath = "//*[contains(@class, 'bottom-container')]"
container = driver.find_element(By.XPATH, container_xpath)

# Locate all input elements within the container
input_elements = container.find_elements(By.CSS_SELECTOR, 'div[contenteditable="true"]')

# List to store successfully processed elements
successful_elements = []

# Send keys to each input element and store successful ones
for index, element in enumerate(input_elements):
    try:
        element.send_keys(f"tell me a story in Japanese {index + 1}")
        print(f"Sent keys to input {index + 1}")
        successful_elements.append(element)  # Store the successful element
        element.send_keys(Keys.RETURN)  # Simulate pressing the Enter key
    except Exception as e:
        print(f"Failed to send keys to input {index + 1}: {e}")

# Optionally, do something with successful elements
for elem in successful_elements:
    print(f"Successfully processed element: {elem}")

# Keep the browser open for a while to observe
time.sleep(10000)
