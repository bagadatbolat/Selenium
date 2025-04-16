
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions() # создаем переменную option для дальнейшего переиспользования
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

base_url = "https://www.saucedemo.com/" # создаем переменную base_url для дальнейшего переиспользования
driver.get(base_url) # передаем переменную base_url драйверу, чтобы он смог открыть ссылку
driver.maximize_window() # задаем разрешение,с которой драйвер откроет окно веб-браузера