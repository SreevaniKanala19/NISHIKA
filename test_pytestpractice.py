import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import pdb

@pytest.fixture
def test_opening_page():
    driver = webdriver.Chrome(executable_path=r"C:\Users\HP\OneDrive\Desktop\vani\chromedriver_win32\chromedriver.exe")
    time.sleep(3)
    driver.get('https://gramawardsachivalayam.ap.gov.in/GSWS/Home/Main')
    time.sleep(2)
    driver.maximize_window()
    driver.find_element(By.XPATH,'//*[@id="navbarDropdown"]').click()
    driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/ul/li[3]/ul/li[4]/a').click()
    time.sleep(5)
    print(driver.current_window_handle)
    chwnd = driver.window_handles[1]
    driver.switch_to.window(chwnd)
    time.sleep(3)
    driver.find_element(By.XPATH,'//*[@id="user-name"]').send_keys('11190008-DA')
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('Rojudu@101910')
    driver.find_element(By.XPATH,'//*[@id="save"]').click()
    time.sleep(5)
    yield driver
    driver.quit()
@pytest.mark.smoke
def test_regularize(test_opening_page):
    driver = test_opening_page
    driver.find_element(By.XPATH,'//*[@id="leave-from_date"]').send_keys('04/07/2022')
    driver.find_element(By.XPATH,'//*[@id="leave-to_date"]').send_keys('05/07/2022')
    elm = driver.find_element(By.XPATH,'//*[@id="reason"]')
    drp = Select(elm)
    drp.select_by_visible_text('On Duty')
    driver.find_element(By.XPATH,'//*[@id="remarks"]').send_keys('Training in SRO office,Badvel')
    time.sleep(2)
    elm = driver.find_element(By.XPATH,'//*[@class="btn btn-primary rounded-0" and text()="Regularize"]')
    driver.execute_script('arguments[0].click();',elm)

    time.sleep(20)




