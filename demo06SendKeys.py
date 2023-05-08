from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

PATH = "D:\Software_Environment\chromedriver\v113\chromedriver.exe"

driver = webdriver.Chrome(options=options)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.find_element(By.CSS_SELECTOR, "[value='radio2']").click()
input_field = driver.find_element(By.XPATH, "//input[@id='name']")
input_field.send_keys("Phuc Do")
input_field.clear()    
input_field.send_keys("Liem Nguyen")

alert_example = driver.find_element(By.XPATH, "//legend[text()='Switch To Alert Example']")
alert_example_text = alert_example.text
print(alert_example_text)