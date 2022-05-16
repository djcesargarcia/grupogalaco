from multiprocessing.connection import wait
from selenium import webdriver
driver = webdriver.Chrome("C:/Users/pit/Desktop/web/grupogalaco/grupogalaco/testselenium/chromedriver_win32/chromedriver")
driver.get("https://www.wikipedia.org")
title = driver.title
wait(10)
driver.close()