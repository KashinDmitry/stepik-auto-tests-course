import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

hidden_message = ''


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(7)
    yield browser
    print("\nquit browser..")
    print("hidden message: ", hidden_message)
    browser.quit()


class TestTask():
    answer = math.log(int(time.time()))

    @pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                      "https://stepik.org/lesson/236896/step/1",
                                      "https://stepik.org/lesson/236897/step/1",
                                      "https://stepik.org/lesson/236898/step/1",
                                      "https://stepik.org/lesson/236899/step/1",
                                      "https://stepik.org/lesson/236903/step/1",
                                      "https://stepik.org/lesson/236904/step/1",
                                      "https://stepik.org/lesson/236905/step/1"])
    def test_find_hidden_message(self, browser, link):
        global hidden_message
        browser.get(link)
        answer = math.log(int(time.time()))

        # find a field and send the answer
        browser.find_element_by_class_name('ember-text-area').send_keys(str(answer))

        # click on submit button
        browser.find_element_by_class_name('submit-submission').click()

        # wait for confirmation message and copy a confirmation text
        result = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))).text

        # compare confirmation text with template
        try:
            assert result == 'Correct!', f'Wrong expected message. Should be "Correct!", got "{result}" instead'
        except AssertionError:
            hidden_message += result
            raise  # raise because I want to mark failed test as failed. Without raise all tests are passed despite of AssertionError
