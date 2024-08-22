from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:\\Program Files\\Google\\Chrome\\chromedriver-win64\\chromedriver.exe"

# Specify the path to the Chrome browser executable
chrome_binary_path = "C:\\Users\\pc\\Documents\\chromedriver\\chrome-win64\\chrome-win64\\chrome.exe"

# Set Chrome options
chrome_options = Options()
chrome_options.binary_location = chrome_binary_path
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the ChromeDriver service
service = Service(executable_path=chrome_driver_path, log_path='chromedriver.log')

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open the web page
    driver.get("https://gemini.google.com/app")

    # Wait for the container to be present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.input-area-container[_ngcontent-ng-c3330407648]'))
    )

    # Locate all input elements
    container_selector = '.input-area-container[_ngcontent-ng-c3330407648]'
    input_elements = driver.find_elements(By.CSS_SELECTOR, f"{container_selector} input")

    # Send keys to each input element
    for index, element in enumerate(input_elements):
        try:
            element.send_keys(f"Test input {index + 1}")
            print(f"Sent keys to input {index + 1}")
        except Exception as e:
            print(f"Failed to send keys to input {index + 1}: {e}")

finally:
    # Keep the browser open for manual inspection
    input("Press Enter to close the browser...")
    driver.quit()  # Ensure the browser is closed only after manual inspection
