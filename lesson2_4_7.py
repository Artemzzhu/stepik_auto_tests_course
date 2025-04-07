from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time 

try: 
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока цена не будет равна 100$
    WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    
    button1 = browser.find_element(By.ID, "book")
    button1.click()

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)	

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    
    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()