from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

import time
driver = webdriver.Chrome(executable_path=r"C:\Users\HP\OneDrive\Desktop\vani\chromedriver_win32\chromedriver.exe")
driver.get("https://gramawardsachivalayam.ap.gov.in/GSWS/Home/Main")
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="text"]/div/div[1]/div/div[3]/div/div/div/h5/label/a[1]/u').click()
driver.maximize_window()
print(driver.current_window_handle)
print(driver.window_handles)
chwnd = driver.window_handles[1]
driver.switch_to.window(chwnd)
driver.find_element(By.XPATH,'//*[@id="menu"]/ul/li[4]/a').click()
print(driver.current_window_handle)
driver.find_element(By.XPATH,'//*[@name="loginfmt"]').send_keys('11190008-da@apgsws.onmicrosoft.com')
driver.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
time.sleep(5)
driver.quit()



driver.quit()