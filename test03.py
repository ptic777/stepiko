import math
 import time
 from selenium import webdriver
 from selenium.webdriver.remote.webelement import WebElement

 browser = webdriver.Firefox()
 link = "http://suninjuly.github.io/alert_accept.html"


 def calc(x):
     return str(math.log(abs(12 * math.sin(int(x)))))

 try:
     browser.get(link)
     button = browser.find_element_by_xpath("//button")
     button.click()

     alert = browser.switch_to_alert()
     alert.accept()
     print("Y =")
     time.sleep(1)
     x_element = browser.find_element_by_id("input_value")
     x = x_element.text
     y = calc(x)
     print ("После поиска ",y)

     amsw1 = browser.find_element_by_id('answer')
     amsw1.send_keys(y)
     but1 = browser.find_element_by_xpath("//button")
     but1.click()

 finally:
     time.sleep(10)
     browser.quit()
