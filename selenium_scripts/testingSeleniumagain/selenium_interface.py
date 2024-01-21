from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

class SeleniumInterface:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, timeout=2)
        self.waitlonger = WebDriverWait(self.driver, timeout=30)
        self.url = url
        

    def load_website(self):
        self.driver.get(self.url)

    def wait_for_element(self, by, value):
        try:
            element = self.waitlonger.until(EC.presence_of_element_located((by, value)))
            return element
        except TimeoutException:
            print(f"Timed out waiting for element {value} to be located")

    def click_element(self, by, value):
        try:
            element = self.wait_for_element(by, value)
            element.click()
        except TimeoutException:
            print(f"Timed out waiting for element {value} to be clickable")

    # def send_keys_to_element(self, by, value, keys):
    #     try:
    #         self.wait_for_element(by, value).send_keys(keys)
    #     except TimeoutException:
    #         print(f"Timed out waiting for element {value} to be located")

    def get_element_text(self, by, value):
        try:
            element = self.wait_for_element(by, value)
            return element.text
        except TimeoutException:
            print(f"Timed out waiting for element {value} to be located")

    def run_google_fiber_test(self, debug=0):
        self.load_website()
        self.click_element(By.XPATH, '//*[@id="main-content"]/div[1]/div/button')
        download_speed = self.get_element_text(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[1]/div[2]/div[1]/div[2]/div[1]/div/span')
        upload_speed = self.get_element_text(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[1]/div[2]/div[2]/div[2]/div[1]/div/span')
        ping = self.get_element_text(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[1]/div[1]/div[1]/div[2]/div/div/span')
        jitter = self.get_element_text(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[1]/div[1]/div[2]/div[2]/div/div/span')

        print("yay")
        self.driver.quit()
        if debug == 0:
            return(download_speed, upload_speed, ping, jitter)
        else:
            provider = self.get_element_text(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[2]/div[1]/div/div[1]/div[2]/div[1]/span')
            ip = self.get_element_text(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[2]/div[1]/div/div[1]/div[2]/div[2]/span')
            location = self.get_element_text(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[2]/div[1]/div/div[3]/div[2]/div[2]/span/span')
            return(download_speed, upload_speed, ping, jitter, provider, ip, location)

# gfibertest = SeleniumInterface('https://gfiber.speedtestcustom.com/')
# gfibertest.run_google_fiber_test()
