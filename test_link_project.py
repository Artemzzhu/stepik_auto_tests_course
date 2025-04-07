from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestLink(unittest.TestCase):
    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first[required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.form-control.second[required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.third[required]")
        input3.send_keys("a@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        browser.quit()

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Warning")

    def test_link2(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first[required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.form-control.second[required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.third[required]")
        input3.send_keys("a@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        browser.quit()

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Warning")


if __name__ == "__main__":
    unittest.main()