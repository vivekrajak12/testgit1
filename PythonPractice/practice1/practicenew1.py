

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#serv_obj=Service("F:\driver browser epam\chromedriver_win32\chromedriver.exe")
#driver=webdriver.Chrome(service=serv_obj)
#serv_obj=Service("F:\driver browser epam\geckodriver-v0.31.0-win64\geckodriver.exe")
#driver=webdriver.Firefox(service=serv_obj)
serv_obj=Service("F:\driver browser epam\edgedriver_win64\msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)
driver.get("https://www.google.com")
driver.find_element(By.)
driver.find_element(By.XPATH("//*[name="btnk"]")).click()