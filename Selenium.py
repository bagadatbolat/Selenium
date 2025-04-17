import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# создаем переменную base_url для дальнейшего переиспользования
base_url = "https://www.saucedemo.com/"

# Открытие сайта в Google Chrome
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome_driver.get(base_url)
chrome_driver.maximize_window() # задаем разрешение,с которой драйвер откроет окно веб-браузера

# Открытие сайта в Mozilla Firefox
firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
firefox_driver.get(base_url)
firefox_driver.maximize_window() # задаем разрешение,с которой драйвер откроет окно веб-браузера

# Открытие сайта в Microsoft Edge
edge_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
edge_driver.get(base_url)
edge_driver.maximize_window() # задаем разрешение,с которой драйвер откроет окно веб-браузера