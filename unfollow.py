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

# Twitter login credentials
username = '@tay8789'
password = 'Nitay@8789'

# Initialize the Chrome driver
driver = webdriver.Chrome(service=ChromeService(executable_path=webdriver_path))
wait = WebDriverWait(driver, 100)

# Navigate to Twitter login page
driver.get("https://x.com/login")

# Wait for the page to load
time.sleep(5)

# Log in to Twitter
username_field = driver.find_element(By.NAME, "text")
username_field.send_keys(username)
username_field.send_keys(Keys.RETURN)
time.sleep(3)

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)
time.sleep(3)

# Navigate to the user's profile
driver.get("https://x.com/BarackObama")

# Locate the unfollow button
unfollow_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/button/div/span/span')))

# Click the unfollow button
unfollow_button.click()

# Confirm unfollow action (a confirmation dialog may appear)
confirm_unfollow_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/button[1]/div/span')))
confirm_unfollow_button.click()
print("unfollowed successfully")

# Wait for a few seconds to ensure the unfollow action is complete
time.sleep(5)

# Close the browser
driver.quit()