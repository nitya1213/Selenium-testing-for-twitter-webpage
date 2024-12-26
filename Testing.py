from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup ChromeDriver
chromedriver_path = 'C:\\Program Files (x86)\\chromedriver.exe'  # Adjust this path as needed
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open the login page
    driver.get("https://x.com/i/flow/login")
    print(f"Opened page: {driver.title}")

    # Wait for the username field to be present
    wait = WebDriverWait(driver, 20)
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "text")))
    print("Username field located.")

    # Enter the username and submit
    username_field.send_keys("@tay8789" + Keys.ENTER)
    print("Username entered.")

    # Wait for the password field to be present
    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    print("Password field located.")

    # Enter the password and submit
    password_field.send_keys("Nitay@8789" + Keys.ENTER)
    print("Password entered.")

    # Wait for a successful login indication
    success_indicator = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Home')]")))
    print("Login success indicator located.")

    # Print the title of the page after login
    print(f"Page title after login: {driver.title}")

    # Verify login success
    if "Home / X" in driver.title:  # Adjust the title as needed
        print("Login successful")
    else:
        print("Login failed")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()