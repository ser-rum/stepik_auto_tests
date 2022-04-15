from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get('https://www.dns-shop.ru')
    search = browser.find_element_by_class_name('ui-input-search__input ui-input-search__input_presearch')

finally:
    browser.quit()