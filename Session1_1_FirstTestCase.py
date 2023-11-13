#Test case
# 1) Open Web Browers (Chrome/Firefox/Edge)
# 2) Open 1 URL login 
# 3) Enter username (Admin)
# 4) Enter password (admin123)
# 5) Click Login 
# 6) Capter Title of the home page (Actual Title) 
# 7) Verify title of the page: OrangeHRM (Expected)
# 8) Close Brower
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('D:\PYTHON_LEARNING\Python_Selenium\chromedriver.exe')
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
sleep(3)

driver.find_element_by_name('username').send_keys("Admin")
driver.find_element_by_name('password').send_keys("admin123")
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

sleep(3)
act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Fail")

driver.close()

'''
for i in range(2,5):
    print(i)
    print(type(i))