import math
from selenium import webdriver
from selenium.webdriver.common.by import By

path = r"C:\project\chromedriver3.exe"

link = "http://suninjuly.github.io/find_xpath_form"

browser = webdriver.Chrome(executable_path = path)
browser.get(link)

input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name("form-control.city")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")
button = browser.find_element(By.XPATH, "//button[@type='submit']")
button.click()

