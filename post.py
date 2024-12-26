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

# Navigate to Twitter login page
driver.get("https://x.com/login")

# Wait for the page to load
time.sleep(10)

# Log in to Twitter
username_field = driver.find_element(By.NAME, "text")
username_field.send_keys(username)
username_field.send_keys(Keys.RETURN)
time.sleep(10)

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)
time.sleep(10)

# Navigate to the tweet composition area
driver.get("https://x.com/compose/tweet")
time.sleep(10)

# Locate the tweet input field
tweet_input = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')

# Compose and post a tweet
tweet_text = "Hello, world! This is an automated tweet from Selenium."
tweet_input.send_keys(tweet_text)

# Click the tweet button
tweet_button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]/div/span')
tweet_button.click()

# Wait for the tweet to post
time.sleep(10)

# Print confirmation
print("Tweet posted successfully!")

# Close the browser
driver.quit()