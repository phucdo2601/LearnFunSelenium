from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

PATH = "D:\Software_Environment\chromedriver\v113\chromedriver.exe"

driver = webdriver.Chrome(options=options)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# driver.find_element(By.NAME, "checkboxOption1").click()
# driver.find_element(By.CLASS_NAME, "radioButton").click()
# driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "InterviewQues/ResumeAssistance").click()