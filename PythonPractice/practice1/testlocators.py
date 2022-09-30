from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("F:\driver browser epam\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
driver.find_element(By.ID,"name").send_keys("Vivek")
driver.find_element(By.CSS_SELECTOR,"#phone").send_keys("9988556633")
#driver.find_element(By.XPATH,"//input[@id='email']").send_keys("vivek@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input.form-control[type=email]").send_keys("vi@h.com")
driver.find_element(By.XPATH,"//input[@id='password'and @placeholder='Password']").send_keys("admin123")