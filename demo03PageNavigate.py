from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "D:\Software_Environment\chromedriver\v113\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get('https://www.techwithtim.net/')

link = driver.find_element(By.LINK_TEXT, "Game Development With Python")

link.click()

try:
    element = driver.find_element(By.ID, "sow-button-1931-0003")
    element.click()
    driver.back()
    driver.back()
    driver.back()
    driver.back()
    
except:
    driver.quit()
    
