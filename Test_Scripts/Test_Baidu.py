from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_id("setf").click()
handles=driver.window_handles
for handle in handles:
    if driver.current_window_handle!=handle:
        driver.switch_to.window(handle)
sleep(10)
driver.find_element_by_link_text("百度首页").click()
