from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("https://kyfw.12306.cn/otn/index/init")

js='document.getElementById("train_date").removeAttribute("readonly");'
driver.execute_script(js)

js_value='document.getElementById("train_date").value="2018-12-25"'
driver.execute_script(js_value)