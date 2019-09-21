#selenium education
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

path = r"C:\project\chromedriver3.exe"
url = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome(executable_path = path)
    browser.get(url)

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    result = str(int(num1) + int(num2))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result)
    browser.find_element_by_css_selector("button.btn").click()
finally:
    # time to check result
    time.sleep(100)
    browser.quit()
    print (result)