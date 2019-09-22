# Открыть страницу 
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
# Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = r"C:\project\chromedriver3.exe"

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome(executable_path = path)
	browser.get("http://suninjuly.github.io/explicit_wait2.html")
	button = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "100$")
	)
	browser.find_element_by_id("book").click()

	input1 = browser.find_element_by_id("input_value").text
	input2 = (calc(input1))
	browser.find_element_by_id("answer").send_keys(input2)
	browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
	time.sleep(10)
	browser.quit()

