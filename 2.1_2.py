import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')

x = browser.find_element_by_css_selector('#treasure')
y = calc(x.get_attribute('valuex'))

answer_field = browser.find_element_by_css_selector('#answer')
answer_field.send_keys(y)

robot_checkbox = browser.find_element_by_css_selector('#robotCheckbox')
robot_checkbox.click()

robot_rules = browser.find_element_by_css_selector('#robotsRule')
robot_rules.click()

submit = browser.find_element_by_css_selector("[type='submit']")
submit.click()
