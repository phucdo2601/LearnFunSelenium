from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

PATH = "D:\Software_Environment\chromedriver\v113\chromedriver.exe"

driver = webdriver.Chrome(options=options)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.find_element(By.CSS_SELECTOR, "[value='radio2']").click()