from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def calc(x, y):
  return str(int(x) + int(y))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text
    z = calc(x, y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)
    browser.find_element_by_class_name('btn').click()

    time.sleep(15)

finally:
    browser.quit()