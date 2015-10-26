from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com/")
window_before = driver.window_handles[0]
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
time.sleep(3)
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
driver.get('http://stackoverflow.com/')

time.sleep(3)



