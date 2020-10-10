from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_page_html(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get(url)
    time.sleep(10)
    return driver.page_source