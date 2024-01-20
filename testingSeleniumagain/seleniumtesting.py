from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()

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


try:
    elements = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'result-chart-container')))
except:
    print("Timed out waiting for elements to be located")
print("yay")

driver.quit()
