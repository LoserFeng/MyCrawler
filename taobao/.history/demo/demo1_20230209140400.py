from selenium import webdriver
from time import sleep


driver=webdriver.Chrome()
driver.get('http://baidu.com')
driver.find_element_by_id('kw')
driver.find_element_by_id('su')

