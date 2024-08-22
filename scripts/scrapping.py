# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time


# # Specify the path to the ChromeDriver executable
# chrome_driver_path = "C:\\Program Files\\Google\\Chrome\\chromedriver-win64\\chromedriver.exe"

# # Specify the path to the Chrome browser executable
# chrome_binary_path = "C:\\Users\\pc\\Documents\\chromedriver\\chrome-win64\\chrome-win64\\chrome.exe"

# # Path to your Chrome user data (profile)
# chrome_user_data_dir = "C:\\Users\\pc\\AppData\\Local\\Google\\Chrome for Testing\\User Data"

# # Set Chrome options to use the specific Chrome binary and profile
# chrome_options = Options()
# chrome_options.binary_location = chrome_binary_path
# chrome_options.add_argument(f"--user-data-dir={chrome_user_data_dir}")

# # Set up the ChromeDriver service
# service = Service(executable_path=chrome_driver_path)
 
# # # Initialize the WebDriver with the specified service and options
# driver = webdriver.Chrome(service=service, options=chrome_options)

# web = driver.get("https://gemini.google.com/app") 


# time.sleep(1000000)


# # input_selector = '.input-area[_ngcontent-ng-c756920449]'
# # contact_form = driver.find_element(By.CSS_SELECTOR, input_selector)

# # contact_form.send_keys("Hello, this is a test!")



# # # nav=driver.find_element(By.CLASS_NAME, "class_name")








from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:\\Program Files\\Google\\Chrome\\chromedriver-win64\\chromedriver.exe"

# Specify the path to the Chrome browser executable
chrome_binary_path = "C:\\Users\\pc\\Documents\\chromedriver\\chrome-win64\\chrome-win64\\chrome.exe"

chrome_user_data_dir = "C:\\Users\\pc\\AppData\\Local\\Google\\Chrome\\User Data"

# Set Chrome options to use the specific Chrome binary
chrome_options = Options()
# chrome_options.binary_location = chrome_binary_path
chrome_options.add_argument(f"--user-data-dir={chrome_user_data_dir}")
chrome_options.add_argument("--no-sandbox")  # Disable the sandbox
chrome_options.add_argument("--disable-dev-shm-usage")  # Disable shared memory usage

# Set up the ChromeDriver service
service = Service(executable_path=chrome_driver_path)

# Initialize the WebDriver with the specified service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the web page
driver.get("https://gemini.google.com/app")

# Wait for the page to load and the container to be present
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.input-area-container[_ngcontent-ng-c3330407648]'))
)




# time.sleep(1000000)


# Locate all input elements within the container
container_selector = '.input-area-container[_ngcontent-ng-c3330407648]'
input_elements = driver.find_elements(By.CSS_SELECTOR, f"{container_selector} input")

# Send keys to each input element
for index, element in enumerate(input_elements):
    try:
        element.send_keys(f"Test input {index + 1}")
        print(f"Sent keys to input {index + 1}")
    except Exception as e:
        print(f"Failed to send keys to input {index + 1}: {e}")

# Keep the browser open for manual inspection
# driver.quit()  # Comment or remove this line to keep the session open
