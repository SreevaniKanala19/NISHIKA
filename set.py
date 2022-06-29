import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome(executable_path=r"C:\Users\HP\OneDrive\Desktop\vani\chromedriver_win32\chromedriver.exe")
driver.get('https://gramawardsachivalayam.ap.gov.in/GSWS/Home/Main')
time.sleep(4)
driver.find_element(By.XPATH,'//*[@id="text"]/div/div[1]/div/div[3]/div/div/div/h5/label/a[1]/u').click()
print(driver.current_window_handle)
chwnd = driver.window_handles[1]
driver.switch_to.window(chwnd)
time.sleep(4)
driver.find_element(By.XPATH,'//*[@id="menu"]/ul/li[4]/a').click()
time.sleep(4)
driver.find_element(By.XPATH,'//*[@id="i0116"]').send_keys('11190008-da@apgsws.onmicrosoft.com')
time.sleep(4)
driver.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="i0118"]').send_keys('Rojudu@101910')
driver.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
time.sleep(5)
print(driver.window_handles)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
driver.find_element(By.XPATH,'/html/body/app-root/div/div/div[2]/app-home/app-dashboard/div/div/div[3]/div[1]/div[2]/ul[1]/li[1]/a/span').click()
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/app-root/div/div/div[2]/app-home/app-dashboard/div/div/div[3]/div[1]/div[2]/ul[1]/li[1]/ul/li[4]/a/span').click()
time.sleep(8)
driver.quit()
