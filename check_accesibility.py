import requests
from bs4 import BeautifulSoup

def get_imgs(url):
    # HTML全体を表示する
    parse_url = requests.get(url)
    soup = BeautifulSoup(parse_url.text, 'html.parser')
    imgs = soup.find_all('img')
    
    imgs_alt = [url.get('alt') for url in soup.find_all('img')]
    
def alt_check(url):
    parse_url = requests.get(url)
    soup = BeautifulSoup(parse_url.text, 'html.parser')
    imgs_list = [(img, img.get('alt')) for img in soup.find_all('img')]
    for img in imgs_list:
        if not img[1]:
            print(img[0], 'alt属性が設定されていません') 
alt_check('https://emmoi.net/')
    