from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

path = r"C:\project\chromedriver3.exe"
url = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
try:

