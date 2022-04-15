from selenium import webdriver
import os
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    browser.find_element_by_name('firstname').send_keys('Мишка')
    browser.find_element_by_name('lastname').send_keys('Мишков')
    browser.find_element_by_name('email').send_keys('mishka@mishka.mishka')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'les2_step8.txt')
    browser.find_element_by_id('file').send_keys(file_path)
    button = browser.find_element_by_class_name('btn').click()

    time.sleep(15)

finally:
    browser.quit()