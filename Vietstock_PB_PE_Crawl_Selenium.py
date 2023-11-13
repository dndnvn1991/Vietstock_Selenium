
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os

#Đọc từng dòng trong file txt - Trả về 1 list
#with open('Test.txt','r') as file:  #dung de test 1-2 link truoc
with open('DataLink_Vietstock.txt','r') as file:
     content = file.readlines()
     print(content)
     print('Tong Luong Link:' + len(content))



'''
#C1: Headless Mode: Không work 
options = Options()
options.add_argument("--headless")

C2: Headless Mode: Không work 
ops = webdriver.ChromeOptions()
ops.headless = True
'''

#Chay ChromeDriver

sevr_obj = Service(os.getcwd()+'\chromedriver.exe')
driver = webdriver.Chrome(service=sevr_obj)
driver.implicitly_wait(10)

#Load link - All link chay trong 1 tab
stock_list = []
for link in content: 
    url = link[:-1]  
    driver.get(url)
    try:
        EPS = driver.find_element(By.XPATH,'//*[@id="page-container"]/div[3]/div[1]/div[4]/div/div[5]/div/div/p[1]/b').text
        BVPS = driver.find_element(By.XPATH,'//*[@id="page-container"]/div[3]/div[1]/div[4]/div/div[5]/div/div/p[4]/b').text
        symbol = driver.find_element(By.XPATH,'//*[@id="page-container"]/div[3]/div[1]/div[1]/h1/span/b/a').text
        PB_ratio = driver.find_element(By.XPATH,'//*[@id="page-container"]/div[3]/div[1]/div[4]/div/div[5]/div/div/p[5]/b').text
        PE_ratio = driver.find_element(By.XPATH,'//*[@id="page-container"]/div[3]/div[1]/div[4]/div/div[5]/div/div/p[2]/b').text
        #print(symbol, PE_ratio, PB_ratio)
        stock = {
                'Symnbol': symbol,
                'PB' :  PB_ratio,   
                'PE' :  PE_ratio, 
                'BVPS':   BVPS,
                'EPS'  : EPS,
                }
        stock_list.append(stock)
        print(stock)
    except: 
        print(driver.current_url)


#Kill Process ChromeDriver
driver.quit()

data_ngay ='10.11.2023'

df =  pd.DataFrame(stock_list)
print(df.head(2))

df.to_csv('Vietstock_CrawlData_PBPE_{data}.csv'.format(data =data_ngay), index=False)
#df.to_csv('Test_{data}.csv'.format(data =data_ngay), index=False)


#Báo cáo - Report
print('Total Links: ', len(content))
print('Total Stock Scaping: ',len(df))

