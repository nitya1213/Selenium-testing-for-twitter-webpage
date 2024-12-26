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
wait = WebDriverWait(driver, 30)

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

# Navigate to profile page
driver.get("https://x.com/Tay8789?t=k6PP58crwKzxpQbZSSeG5Q&s=08")

edit_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[2]/a/div/span/span')))
edit_button.click()

# Wait for the profile name field to be present
profile_name_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/label/div/div[2]/div/input')))
new_display_name="Nitya"

# Clear the existing name and enter the new display name
profile_name_field.clear()
profile_name_field.send_keys(new_display_name)

# Save the changes
save_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/button/div/span/span')))
save_button.click()

print("display name changed successfully")

# Wait for the changes to be saved
time.sleep(5)

# Close the browser
driver.quit()