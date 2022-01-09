from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')

x1 = browser.find_element_by_id('num1').text
x2 = browser.find_element_by_id('num2').text
answer = int(x1) + int(x2)

select = Select(browser.find_element_by_id('dropdown'))
select.select_by_value(str(answer))

submit = browser.find_element_by_css_selector("[type='submit']")
submit.click()