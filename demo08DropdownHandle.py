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

# static_dropdown = driver.find_element(By.ID, 'dropdown-class-example')
# select = Select(static_dropdown)
# select.select_by_index(2)
# time.sleep(5)
# select.select_by_visible_text("Option1")
# time.sleep(5)
# select.select_by_value("option3")

static_dropdown_opt2 = driver.find_element(By.XPATH, "//option[@value='option2']")
static_dropdown_opt2.click()