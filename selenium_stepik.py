
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
link = 'http://suninjuly.github.io/explicit_wait2.html'
try:
    driver = webdriver.Chrome()
    driver.get(link)
    WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element(
            (By.ID, 'price'), '100')
    )
    driver.find_element_by_id('book').click()
finally:
    time.sleep(10)
    driver.quit()

