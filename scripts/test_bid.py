# Generated by Selenium IDE

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://localhost:3000/")
driver.set_window_size(1552, 832)
driver.find_element(By.CSS_SELECTOR, ".col:nth-child(1) > .row:nth-child(2) a").click()
driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) .mainImg").click()
driver.find_element(By.ID, "bid").click()
driver.find_element(By.ID, "bid").send_keys("120")
driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)").click()
driver.quit()
