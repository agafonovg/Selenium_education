# Открыть страницу 
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

path = r"C:\project\chromedriver3.exe"
url = "http://suninjuly.github.io/file_input.html"

try:
	browser = webdriver.Chrome(executable_path = path)
	browser.get(url)

	browser.find_element_by_name("firstname").send_keys("First Name")
	browser.find_element_by_name("lastname").send_keys("Lastname")
	browser.find_element_by_name("email").send_keys("email@email.email")
	current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir, 'empty.txt')           # добавляем к этому пути имя файла 
	browser.find_element_by_id("file").send_keys(file_path)
	browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
	time.sleep(10)
	browser.quit()
