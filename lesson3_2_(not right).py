import math
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

path = r"C:\project\chromedriver3.exe"

link = "http://suninjuly.github.io/registration1.html"

browser = webdriver.Chrome(executable_path = path)
browser.get(link)

class Test1(unittest.TestCase):

	def test_fist_name(self):
		browser.find_element_by_tag_name("input").send_keys("First_Name")
		
	def test_second_name(self):	
		browser.find_element_by_class_name("form-control.second").send_keys("last_name")
	
	def test_email(self):	
		browser.find_element_by_class_name("form-control.third").send_keys("email")

	def test_button_to_send(self):	
		browser.find_element(By.XPATH, "//button[@type = 'submit']").click() 


link = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome(executable_path = path)
browser.get(link)

class Test2(unittest.TestCase):

	def test_fist_name2(self):
		browser.find_element_by_tag_name("input").send_keys("First_Name")

	def test_second_name2(self):	
		browser.find_element_by_class_name("form-control.second").send_keys("last_name")
	
	def test_email2(self):	
		browser.find_element_by_class_name("form-control.third").send_keys("email")

	def test_button_to_send2(self):	
		browser.find_element(By.XPATH, "//button[@type = 'submit']").click() 
        
if __name__ == "__main__":
	unittest.main()