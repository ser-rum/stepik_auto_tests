from selenium import webdriver
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_reg1(self):
        welcome_text = registration('http://suninjuly.github.io/registration1.html')
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration didn`t happen.")

    def test_reg2(self):
        welcome_text = registration('http://suninjuly.github.io/registration2.html')
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration didn`t happen.")

def registration(link):
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("div.first_block input.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div.first_block input.second")
    input2.send_keys("Ivanov")
    input3 = browser.find_element_by_css_selector("div.first_block input.third")
    input3.send_keys("Smolensk@smolensk.smolensk")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(5)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    return welcome_text

    time.sleep(10)
    browser.quit()

if __name__ == "__main__":
    unittest.main()