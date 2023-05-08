from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

PATH = "D:\Software_Environment\chromedriver\v113\chromedriver.exe"

driver = webdriver.Chrome(options=options)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

check_boxes = driver.find_elements(By.XPATH, "//input[starts-with(@id, 'checkBoxOption')]")
print(len(check_boxes))
for check_box in check_boxes:
    if check_boxes.index(check_box) + 1 != 2:
        check_box.click()