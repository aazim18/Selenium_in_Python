'''
Created on Sep 22, 2019

@author: anwarul azim
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('http://automationpractice.com/')

driver.maximize_window()

driver.find_element_by_link_text('Women').click()

cat1 = driver.find_element_by_xpath(".//*[@id='layered_category_8']")
cat1.click()



 

