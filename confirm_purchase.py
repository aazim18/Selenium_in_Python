'''
Created on Sep 29, 2019

@author: Anwarul Azim
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('http://automationpractice.com/')

#driver.maximize_window()

driver.find_element_by_link_text('Women').click()

driver.find_element_by_link_text('Faded Short Sleeve T-shirts').click()

#entering quantity
driver.find_element_by_id('quantity_wanted').clear()
element1 = driver.find_element_by_id('quantity_wanted')
element1.send_keys('2')

#Choosing Size
select = Select(driver.find_element_by_id('group_1'))
select.select_by_visible_text('M')

#adding to cart
driver.find_element_by_id("add_to_cart").click()  

#proceed to checkout
          







