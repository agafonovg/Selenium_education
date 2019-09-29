from selenium import webdriver
import time
import pytest

path = r"C:\project\chromedriver3.exe"

def link_t(link):
    browser = webdriver.Chrome(executable_path = path)
    browser.get(link)

    browser.find_element_by_css_selector(".first_block .first").send_keys("First Name")
    browser.find_element_by_css_selector(".first_block .second").send_keys("Second Name")
    browser.find_element_by_css_selector(".first_block .third").send_keys("Email")
    browser.find_element_by_css_selector("button.btn").click()

    time.sleep(1)
    return browser.find_element_by_tag_name("h1").text


class TestReg:
    def test_reg1(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration1.html"),
                "Поздравляем! Вы успешно зарегистировались!", "registration is failed")


    def test_reg2(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration2.html"),
                "Поздравляем! Вы успешно зарегистировались!", "registration is failed")

if __name__ == "__main__":
    pytest.main()