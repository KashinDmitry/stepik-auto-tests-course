from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

price = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '100')
)
book = browser.find_element_by_id('book').click()

x = int(browser.find_element_by_id('input_value').text)
answer = calc(x)

browser.find_element_by_id('answer').send_keys(answer)
browser.find_element_by_css_selector('#solve').click()
