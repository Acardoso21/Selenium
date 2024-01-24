from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
import csv

class SeleniumInterface:
    def __init__(self, url,button_file='selenium_scripts/button_xpaths.csv'):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, timeout=2)
        self.waitlonger = WebDriverWait(self.driver, timeout=60)
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

    def press_tab_and_enter(self, times):
        # navigate to the url
        self.driver.get(self.url)

        # find an element to send keys to
        element = self.driver.find_element(By.TAG_NAME,'body')  # replace this with your preferred element

        for _ in range(times):
            element.send_keys(Keys.TAB)
            time.sleep(0.1)  # wait for 0.1 seconds

        element.send_keys(Keys.ENTER)

    def run_google_fiber_test(self, debug=0):
        self.load_website()
        self.click_element(By.XPATH, '//*[@id="main-content"]/div[1]/div/button')
        download_speed = self.wait_for_element(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[1]/div[2]/div[1]/div[2]/div[1]/div/span').text
        upload_speed = self.wait_for_element(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[1]/div[2]/div[2]/div[2]/div[1]/div/span').text
        ping = self.wait_for_element(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[1]/div[1]/div[1]/div[2]/div/div/span').text
        jitter = self.wait_for_element(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[1]/div[1]/div[2]/div[2]/div/div/span').text
        print("Gfiber Data aquired, moving to next step")
        self.driver.quit()
        if debug == 0:
            return(download_speed, upload_speed, ping, jitter)
        else:
            provider = self.wait_for_element(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[2]/div[1]/div/div[1]/div[2]/div[1]/span').text
            ip = self.wait_for_element(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[2]/div[1]/div/div[1]/div[2]/div[2]/span').text
            location = self.wait_for_element(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[2]/div[1]/div/div[3]/div[2]/div[2]/span/span').text
            return(download_speed, upload_speed, ping, jitter, provider, ip, location)

    def run_speedtest_NET(self,debug=0):
        self.load_website()
        self.wait_for_element(By.ID,'onetrust-consent-sdk')#wait for concent popup
        self.click_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]') #click accpet on consent popup
        self.click_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')#start test
        self.wait_for_element(By.LINK_TEXT, 'You did it! Thank you for helping us reach 50 billion Speedtest results! ')
        # self.press_tab_and_enter(2)
        self.click_element(By.LINK_TEXT, 'Close')#close popup
        download_speed = self.wait_for_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        upload_speed = self.wait_for_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        ping = self.wait_for_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[2]/span').text
        downloadLatency = self.wait_for_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[2]/span').text
        uploadLatency = self.wait_for_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div[2]/div/span[5]/span').text
        jitter = str(abs(int(downloadLatency)-int(uploadLatency)))
        print("speedtest.net Data acquired, moving to next step")
        self.driver.quit()
        if debug == 0:
            return(download_speed, upload_speed, ping, jitter)
        else:
            provider = self.wait_for_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div[2]/div/div[1]/div/div[2]').text
            ip = "Not found"
            location = self.wait_for_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]').text
            return(download_speed, upload_speed, ping, jitter, provider, ip, location)
# gfibertest = SeleniumInterface('https://gfiber.speedtestcustom.com/')
# gfibertest.run_google_fiber_test()
