from selenium import webdriver
from selenium.webdriver.support.ui import Select

 import time


 try:
     link = "http://suninjuly.github.io/selects1.html"
     browser = webdriver.Firefox()
     browser.get(link)
     a = browser.find_element_by_id('num1')
     a1=a.text

     b = browser.find_element_by_id("num2")
     b1 = b.text

     c = int(a1)+int(b1)
     print(c)
     d = str(c)
     print(d)
     select = Select(browser.find_element_by_tag_name("select"))
     select.select_by_visible_text(d)
     button = browser.find_element_by_xpath("// ./ button")
     button.click()

 finally:
     time.sleep(10)
     browser.quit
