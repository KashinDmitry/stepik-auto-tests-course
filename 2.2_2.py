from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/execute_script.html')

answer = calc(int(browser.find_element_by_id('input_value').text))
answer_field = browser.find_element_by_id('answer').send_keys(answer)

robot_checkbox = browser.find_element_by_id('robotCheckbox')
robot_checkbox.click()

browser.execute_script('return arguments[0].scrollIntoView(true);', robot_checkbox)

robot_radio = browser.find_element_by_id('robotsRule').click()
submit = browser.find_element_by_css_selector("[type = 'submit']").click()
