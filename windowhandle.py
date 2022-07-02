from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome(executable_path=r"C:\Users\HP\OneDrive\Desktop\vani\chromedriver_win32\chromedriver.exe")
driver.get('https://the-internet.herokuapp.com/windows')
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="content"]/div/a').click()
time.sleep(4)
print(driver.current_window_handle)
chwnd = driver.window_handles[1]
driver.switch_to.window(chwnd)
time.sleep(5)
driver.quit()
