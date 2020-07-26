import requests
from bs4 import BeautifulSoup

def get_imgs(url):
    # HTML全体を表示する
    parse_url = requests.get(url)
    soup = BeautifulSoup(parse_url.text, 'html.parser')
    imgs = soup.find_all('img')
    
    imgs_alt = [url.get('alt') for url in soup.find_all('img')]
    