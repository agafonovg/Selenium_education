from selenium import webdriver
import time
import unittest

path = r"C:\project\chromedriver3.exe"

def link_t(link):
    browser = webdriver.Chrome(executable_path = path)
    browser.get(link)

    browser.find_element_by_class_name("form-control.first").send_keys("First_name")   
    browser.find_element_by_css_selector('[placeholder = "Input your last name"]').send_keys("last_name")
    browser.find_element_by_css_selector('[placeholder = "Input your email"]').send_keys("email")
    browser.find_element_by_css_selector("button.btn").click()

    time.sleep(1)
    return browser.find_element_by_tag_name("h1").text


class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration1.html"),
                "Поздравляем! Вы успешно зарегистировались!", "registration is failed")


    def test_reg2(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration2.html"),
                "Поздравляем! Вы успешно зарегистировались!", "registration is failed")

if __name__ == "__main__":
    unittest.main()