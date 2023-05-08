from selenium import webdriver
PATH = "D:\Software_Environment\chromedriver\v113\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get('https://www.youtube.com/')
print(driver.title)
driver.quit()   

