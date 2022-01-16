import pytest
from selenium import webdriver
import time


def test_RequiredFieldsPage_1():
    browser = webdriver.Chrome()
    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector(".first_block .first_class [type]")
        first_name.send_keys("wow")

        last_name = browser.find_element_by_css_selector(".first_block .second_class [type]")
        last_name.send_keys("wow")

        email = browser.find_element_by_css_selector(".first_block .third_class [type]")
        email.send_keys("wow")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert welcome_text == "Congratulations! You have successfully registered!", "Wrong congratulation text"

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
    finally:
        browser.quit()

def test_RequiredFieldsPage_2():
    browser = webdriver.Chrome()
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector(".first_block .first_class [type]")
        first_name.send_keys("wow")

        last_name = browser.find_element_by_css_selector(".first_block .second_class [type]")
        last_name.send_keys("wow")

        email = browser.find_element_by_css_selector(".first_block .third_class [type]")
        email.send_keys("wow")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert welcome_text == "Congratulations! You have successfully registered!", "Wrong congratulation text"

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    pytest.main()
