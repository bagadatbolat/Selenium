import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Cоздаем переменную base_url для дальнейшего переиспользования
base_url = "https://www.saucedemo.com/"

# Открытие сайта в Google Chrome
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_driver.get(base_url)
chrome_driver.maximize_window() # задаем разрешение,с которой драйвер откроет окно веб-браузера

# Зполняем поля в странице
user_name = chrome_driver.find_element(By.ID, "user-name")
user_name.send_keys("standard_user")
password = chrome_driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")
