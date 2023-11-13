
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep


sevr_obj = Service('D:\PYTHON_LEARNING\Python_Selenium\chromedriver.exe')
driver = webdriver.Chrome(service=sevr_obj)

driver.get('https://vnexpress.net')
sleep(3)

print(driver.title)
print(driver.current_url)

driver.close()

