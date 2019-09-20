import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")
input2 = browser.find_element_by_class_name('form-control.second') 
#or (By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
input2.send_keys("Petrov")
input3 = browser.find_element(By.XPATH,'/html/body/div/form/div[1]/div[3]/input')
input3.send_keys ("youaracool@eee.com") 
#кажется, я тут накостылили с селектором...но работает. Буду рад критике и как лучше =)
button = browser.find_element(By.XPATH, "//button[@type='submit']")
button.click()

