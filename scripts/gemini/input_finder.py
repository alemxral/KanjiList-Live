from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, WebDriverException

def find_and_send_keys(driver: WebDriver, text: str) -> WebElement:
    """
    Tries to find the correct input element by class name or by iterating over all elements,
    then sends keys to the first valid element it finds.
    
    :param driver: The Selenium WebDriver instance.
    :param text: The text to send to the input element.
    :return: The WebElement to which the text was successfully sent.
    """
    try:
        # First attempt: Find container with a dynamic class name
        container_xpath = "//*[contains(@class, 'bottom-container')]"
        container = driver.find_element(By.XPATH, container_xpath)

        # Find all elements with 'contenteditable="true"' within the container
        input_elements = container.find_elements(By.CSS_SELECTOR, 'div[contenteditable="true"]')

        # Try to send keys to the found elements
        for element in input_elements:
            try:
                element.send_keys(text)
                element.send_keys(Keys.RETURN)  # Press Enter
                return element  # Return the successfully processed element
            except WebDriverException as e:
                print(f"Failed to send keys to an element within container: {e}")
        
        print("No valid input element found within the container.")
    
    except NoSuchElementException:
        print("Container not found by class name. Trying all elements on the page.")
    
    # If the container was not found or no element within it worked, try all elements on the page
    all_elements = driver.find_elements(By.CSS_SELECTOR, 'div[contenteditable="true"]')
    
    for element in all_elements:
        try:
            element.send_keys(text)
            element.send_keys(Keys.RETURN)  # Press Enter
            return element  # Return the successfully processed element
        except WebDriverException as e:
            print(f"Failed to send keys to an element on the page: {e}")
    
    raise Exception("No valid input element found on the page.")

