from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_text_from_response_container(driver: WebDriver, timeout: int = 10) -> list:
    """
    Extracts text from elements within a container that approximately matches certain tag names.
    
    :param driver: Selenium WebDriver instance.
    :param timeout: The maximum amount of time to wait for elements to be present.
    :return: A list of strings containing the text from each response container.
    """

    extracted_texts = []

    try:
        # Use XPath to locate elements that approximately match the tag names
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(name(), 'model-response')]//*[contains(name(), 'response-container')]"))
        )

        # Locate all matching response containers
        response_containers = driver.find_elements(By.XPATH, "//*[contains(name(), 'model-response')]//*[contains(name(), 'response-container')]")

        # Extract and print text from each response container
        for container in response_containers:
            try:
                text = container.text
                extracted_texts.append(text)
                print(f"{text}")
            except Exception as e:
                print(f"Script Error:Failed to extract text from container: {e}")

    except Exception as e:
        print(f"Script Error:Failed to locate response containers: {e}")

    return extracted_texts
