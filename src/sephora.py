import requests
from bs4 import BeautifulSoup
import os
from src.tools.tools import get_page_html
 
class Sephora:
    url = 'https://www.sephora.com/ca/en'
    #url = 'https://www.sephora.com/ca/en/shop/moisturizing-cream-oils-mists?pageSize=300'
    def __init__(self):
        pass

    def get_urls(self) -> dict:
        #r = requests.get(self.url, timeout=(3.05, 27))
        #soup = BeautifulSoup(r.content, 'html.parser')
        #skincare_class_name = soup.find('a', {'href': '/shop/skincare'})
        #skincare_class_name = soup.find('div', {'class': 'css-1wsdzbz e65zztl0'}, recursive=True)
        #.find_all('a', href=True)
        #print(skincare_class_name)
        html = get_page_html(self.url)
        soup = BeautifulSoup(html, 'html.parser')
        skincare_html = soup.find('a', {'href': '/shop/skincare'}).parent.find_all('a', {'class': 'css-xhp3g2'})
        skincare_urls = list(filter(lambda x: '/shop/' in x,map(lambda x: f'{self.url}{x.get("href")}', skincare_html)))
        print(skincare_urls)
