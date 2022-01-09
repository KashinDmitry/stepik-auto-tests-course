from selenium import webdriver
import os


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')


first_name = browser.find_element_by_name('firstname').send_keys('Dmitry')
last_name = browser.find_element_by_name('lastname').send_keys('Kashin')
email = browser.find_element_by_name('email').send_keys('KashinDmitry@mail.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'upload.txt')

choose_file = browser.find_element_by_id('file').send_keys(file_path)

submit = browser.find_element_by_css_selector("[type = 'submit']").click()

