from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get('http://baidu.com')
driver.find_element(by=By.ID,value='kw').send_keys('selenium')
driver.find_element('su').click()


sleep(3)

driver.quit()


