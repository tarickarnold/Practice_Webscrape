from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Locate webdriver for Chrome is folder and start service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

#Launch Chrome browser and go to Google.com
driver.get("https://google.com")

#Delay
WebDriverWait(driver,15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))

#Locate search bar and populate text
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("Phillips 66" + Keys.ENTER)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Phillips 66")))

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Phillips 66")
link.click()

#Delay
time.sleep(8)

#Close browser
driver.quit()


if __name__=="__main__":
    print("This is a script.")
else: print("This is a module.")