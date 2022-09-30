import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("F:\driver browser epam\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
#driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

#driver.find_element(By.ID,"login1").send_keys("vivek@g.com")
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
time.sleep(2)
#driver.find_element(By.NAME,"passwd").send_keys("Admin123")
#driver.find_element(By.CLASS_NAME,"signinbtn").click()
driver.find_element(By.XPATH,"//button[@type='submit']").click()





