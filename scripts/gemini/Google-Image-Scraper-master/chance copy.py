# Import necessary libraries
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
from webdriver_initializer import initialize_webdriver

# Main function to click on all elements under <div id="search">
def click_elements():
    # Initialize WebDriver using your custom initializer
    driver = initialize_webdriver(headless=True)[0]  # Set headless to True
    url = "https://www.google.com/search?q=cats&source=lnms&tbm=isch"
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    # Find the <div> with id="search"
    search_div = driver.find_element(By.ID, "search")

    # Store elements that do not produce errors
    clickable_elements = []

    # Iterate over all child elements of <div id="search">
    for element in search_div.find_elements(By.XPATH, ".//*"):
        try:
            # Skip elements within <a> tags to avoid redirection or new tab opening
            if element.tag_name == 'a':
                href = element.get_attribute('href')
                target = element.get_attribute('target')

                # Check if href or target suggests it opens a new tab or redirects
                if href and ("javascript:" in href.lower() or "window.open" in href.lower()):
                    print("[INFO] Skipping <a> element with JavaScript function in href.")
                    continue
                if target and target.lower() == "_blank":
                    print("[INFO] Skipping <a> element with target='_blank'.")
                    continue
            
            # Attempt to click the element
            element.click()
            time.sleep(1)  # Give time to see the effect of the click
            clickable_elements.append(element)
        except WebDriverException:
            # Log a short warning message if the element cannot be clicked
            print("[WARNING] Could not click element.")

    # Print the number of elements that were clicked successfully
    print(f"[INFO] Successfully clicked {len(clickable_elements)} elements.")

    # Close the WebDriver
    driver.quit()

# Run the function
if __name__ == "__main__":
    click_elements()
