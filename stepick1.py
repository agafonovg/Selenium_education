#selenium education
from selenium import webdriver
import time
import math

path = r"C:\project\chromedriver3.exe"
url = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome(executable_path = path)
    browser.get(url)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")

   

finally:
    # time to check result
    time.sleep()
    browser.quit()
    print (num1)
    print (num2)