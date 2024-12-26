from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time

webdriver_path = 'C:\\Program Files (x86)\\chromedriver.exe'

username = '@tay8789'
password = 'Nitay@8789'

# URL of the post you want to like
post_url = 'https://x.com/taylorswift13/status/1781171613058097619'

# Setup WebDriver
driver = webdriver.Chrome(service=ChromeService(executable_path=webdriver_path))
wait = WebDriverWait(driver, 3)

def login_to_twitter():
    try:
        # Open the login page
        driver.get("https://x.com/i/flow/login")
        print(f"Opened page: {driver.title}")

        # Wait for the username field to be present
        username_field = wait.until(EC.presence_of_element_located((By.NAME, "text")))
        print("Username field located.")

        # Enter the username and submit
        username_field.send_keys(username + Keys.ENTER)
        print("Username entered.")

        # Wait for the password field to be present
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        print("Password field located.")

        # Enter the password and submit
        password_field.send_keys(password + Keys.ENTER)
        print("Password entered.")

        # Wait for a successful login indication
        success_indicator = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Home']")))
        print("Login success indicator located.")

        # Print the title of the page after login
        print(f"Page title after login: {driver.title}")
    except TimeoutException:
        print("Loading took too much time or an element was not found.")
    except Exception as e:
        print(f"An error occurred during login: {e}")

def like_tweet(post_url):
    try:
        # Navigate to the specific post
        driver.get(post_url)
        print(f"Opened post: {post_url}")

        # Wait for the like button to be visible
        like_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='like']"))
        )

        # Scroll to the like button and click it
        ActionChains(driver).move_to_element(like_button).click(like_button).perform()
        print("Liked the post successfully.")

    except TimeoutException:
        print("Loading took too much time or an element was not found.")
    except NoSuchElementException:
        print("An element was not found on the page.")
    except ElementClickInterceptedException:
        print("Element click was intercepted.")
    except Exception as e:
        print(f"An error occurred: {e}")

try:
    login_to_twitter()
    like_tweet(post_url)
finally:
    # Close the WebDriver
    time.sleep(5)  # Wait a few seconds before closing for demonstration purposes
    driver.quit()