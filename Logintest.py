'''
Created on Sep 22, 2019

@author: Anwarul Azim
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://automationpractice.com/')

driver.maximize_window()

link1 = driver.find_element_by_link_text('Sign in')
link1.click()

element1 = driver.find_element_by_id('email')
element1.send_keys('qatest1866@protonmail.com')

element2 = driver.find_element_by_id('passwd')
element2.send_keys('qatest')

logbutton = driver.find_element_by_id('SubmitLogin')
logbutton.click()



