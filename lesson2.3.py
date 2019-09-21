#selenium education
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

path = r"C:\project\chromedriver3.exe"
url = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome(executable_path = path)
	browser.get(url)

	browser.find_element(By.XPATH, "//button[@type='submit']").click()
	confirm = browser.switch_to.alert
	confirm.accept()
	input1 = browser.find_element_by_id("input_value").text
	input2=(calc(input1))
	browser.find_element_by_id("answer").send_keys(input2)
	browser.find_element(By.XPATH, "//button[@type='submit']").click()
finally:
	time.sleep(10)
	browser.quit()
