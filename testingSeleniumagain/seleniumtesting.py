from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
# Specify the path to the WebDriver executable
# Replace 'path/to/chromedriver' with the actual path to the chromedriver executable on your machine

# Set desired capabiliti
# Create a WebDriver instance with desired capabilities
driver = webdriver.Chrome()

# Open a website
wait = WebDriverWait(driver, 20)  # 10 seconds timeout
url = 'https://fiber.google.com/speedtest/'
driver.get(url)
actions = ActionChains(driver)
time.sleep(1)
actions.send_keys(Keys.TAB)
# time.sleep(1)
actions.send_keys(Keys.TAB)
# time.sleep(1)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.TAB)
time.sleep(1)
actions.send_keys(Keys.ENTER)
time.sleep(1)
actions.perform()
# try:
#     print('trying the first way')
#     wait.until(EC.presence_of_all_elements_located())
#     driver.find_element(By.ID, '<button class="button background-primary-hover text-primary" aria-label="GO, start your Speedtest"><span style="font-size: unset; overflow-wrap: unset;">GO</span></button>')
# except:
time.sleep(20)
print('helo')
# go =  driver.find_element(By.NAME, 'GO')
# wait.until(EC.element_to_be_clickable(go))
# Locate the button using its ID (you can use other locators as needed)
# button = driver.find_element(By.ID, 'button_id')

# Click the button
# button.click()

# Wait for a specific element to be present after clicking the button (adjust the timeout as needed)
try:
    wait.until(EC.presence_of_all_elements_located())
    element = wait.until(EC.presence_of_element_located('AGAIN'))
except:
    element = wait.until(EC.presence_of_element_located('progress progress--finished'))
    
# Alternatively, you can use other expected_conditions like visibility_of_element_located, etc.

# Close the browser window
driver.quit()
