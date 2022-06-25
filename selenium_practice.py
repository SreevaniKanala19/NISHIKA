from selenium import webdriver
import time

from selenium.webdriver.common.by import By
user = '11190008-da@apgsws.onmicrosoft.com'
passw = 'Rojudu@101910'

driver = webdriver.Chrome(executable_path=r"C:\Users\HP\OneDrive\Desktop\vani\chromedriver_win32\chromedriver.exe")
driver.get('https://vswsonline.ap.gov.in/')
print(driver.title)
print(driver.name)
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="menu"]/ul/li[4]/a').click()
time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="i0116"]').send_keys(user)
time.sleep(5)
driver.find_element(By.XPATH,'//*[@type="submit"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="i0118"]').send_keys(passw)
time.sleep(8)
driver.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
time.sleep(8)
driver.quit()
# driver.get('https://www.amazon.in/')
# print(driver.title)
# print(driver.name)
# time.sleep(4)
# driver.find_element(By.XPATH,'//*[@id="nav-signin-tooltip"]/a/span').click()
# time.sleep(4)
# driver.find_element(By.XPATH,'//*[@id="ap_email"]').send_keys(user)
# time.sleep(4)
# driver.find_element(By.XPATH,'//*[@id="continue"]').click()
# time.sleep(4)
# #//*[@id="ap_password"]
# # //*[@id="signInSubmit"]
# driver.find_element(By.XPATH,'//*[@id="ap_password"]').send_keys(passw)
# time.sleep(4)
# driver.find_element(By.XPATH,'//*[@id="signInSubmit"]').click()
# time.sleep(4)
# # //*[@id="twotabsearchtextbox"] - search
# # //*[@id="nav-search-submit-button"] - click
# driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]').send_keys('Boat earphones')
# time.sleep(4)
# driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]').click()
# time.sleep(4)
# driver.quit()