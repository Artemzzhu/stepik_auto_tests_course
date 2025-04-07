from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    input1.send_keys("Кристина")
    input2 = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    input2.send_keys("Кошаева")
    input3 = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    input3.send_keys("koshaevva@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')
    f = browser.find_element(By.CSS_SELECTOR, "#file")
    f.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()