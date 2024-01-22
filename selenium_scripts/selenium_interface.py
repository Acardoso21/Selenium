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
        with open(button_file, 'r') as file:
            reader = csv.reader(file)
            self.button = list(reader)
        print(self.button)
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

    def run_google_fiber_test2(self, debug=0):
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
     
    def run_google_fiber_test(self, debug=0):
        self.load_website()
        # print("self button 0,0 " + self.button[0][0])
        n=0
        while n<6:
            print(str(self.button[0][n].strip()))
            n+=1
        self.click_element(By.XPATH, str(self.button[0][1].strip()))
        download_speed = self.wait_for_element(By.XPATH, By.XPATH, str(self.button[0][2].strip())).text
        upload_speed = self.wait_for_element(By.XPATH, By.XPATH, self.button[0][3].strip()).text
        ping = self.wait_for_element(By.XPATH, By.XPATH, self.button[0][4].strip()).text
        jitter = self.wait_for_element(By.XPATH, By.XPATH, self.button[0][5].strip()).text
        print("Gfiber Data aquired, moving to next step")
        self.driver.quit()
        if debug == 0:
            return(download_speed, upload_speed, ping, jitter)
        else:
            provider = self.wait_for_element(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[2]/div[1]/div/div[1]/div[2]/div[1]/span').text
            ip = self.wait_for_element(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[2]/div[1]/div/div[1]/div[2]/div[2]/span').text
            location = self.wait_for_element(By.XPATH, '//*[@id="root"]/div/span/div[2]/div[1]/main/section[2]/div[1]/div/div[3]/div[2]/div[2]/span/span').text
            return(download_speed, upload_speed, ping, jitter, provider, ip, location)

    # def run_
# gfibertest = SeleniumInterface('https://gfiber.speedtestcustom.com/')
# gfibertest.run_google_fiber_test()
