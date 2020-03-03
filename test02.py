 import os
 import time
 from selenium import webdriver
 browser = webdriver.Firefox()
 link = "http://suninjuly.github.io/file_input.html"


 try:
     browser.get(link)
     input1 = browser.find_element_by_name("firstname")
     input1.send_keys("Жора")
     input2 = browser.find_element_by_name("lastname")
     input2.send_keys("Туполев")
     input3 = browser.find_element_by_name('email')
     input3.send_keys('a@a.aa')

     current_dir = os.path.abspath(os.path.dirname(__file__))
     file_path = os.path.join(current_dir, 'test.txt')
     element = browser .find_element_by_id("file")
     element .send_keys(file_path)
     print(os.path.abspath(__file__))
     print(os.path.abspath(os.path.dirname(__file__)))


     button = browser.find_element_by_xpath("//button")
     button.click()

 finally:
     time.sleep(7)
     browser.quit()
