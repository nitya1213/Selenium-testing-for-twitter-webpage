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

# Navigate to messages
driver.get("https://x.com/messages")

chat = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[1]/div/div/div[2]/section/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]/div')))
chat.click()

chat_area=wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div/div/div[2]/div/div/aside/div[2]/div[2]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))

# Compose and send a chat
text = "Hello, world! This is an automated text from Selenium sent by Pujitha and Nitya."
chat_area.send_keys(text)
chat_area.send_keys(Keys.RETURN)

# Wait for the chat to be sent
time.sleep(5)

# Print confirmation
print("chat sent successfully!")

# Close the browser
driver.quit()