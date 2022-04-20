import pytest
from selenium import webdriver
import time
import math

answer = math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")

@pytest.mark.parametrize('lesson', [236895])
def test_guest_should_see_login_link(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    textarea = browser.find_element_by_class("textarea")
    textarea.send_keys(answer)
    browser.find_element_by_class("button").click()
    


'''', 236896, 236897, 236898, 236899, 236903, 236904, 236905'''