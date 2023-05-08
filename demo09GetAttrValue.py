import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option("detach", True)

PATH = "D:\Software_Environment\chromedriver\v113\chromedriver.exe"

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

blinking_link = driver.find_element(By.CLASS_NAME, 'blinkingText')
print(blinking_link.get_attribute('href'))