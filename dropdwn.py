import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\OneDrive\Desktop\vani\chromedriver_win32\chromedriver.exe")
act = ActionChains(driver)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
elm = driver.find_element(By.XPATH,'//*[@id="speed"]')
drp = Select(elm)
drp.select_by_visible_text('Fast')
time.sleep(5)
double = driver.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')
act.double_click(double).perform()
time.sleep(5)
s = driver.find_element(By.XPATH,'//*[@id="draggable"]/p')
d = driver.find_element(By.XPATH,'//*[@id="droppable"]')
act.drag_and_drop(s,d).perform()
time.sleep(3)
driver.quit()