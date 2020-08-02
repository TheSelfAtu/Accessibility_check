import requests
from bs4 import BeautifulSoup

def parse_html(url):
    # HTML全体を表示する
    parse_url = requests.get(url)
    soup = BeautifulSoup(parse_url.text, 'html.parser')
    return soup

# alt属性が存在しないタグをチェック
def alt_none(parse_html):
    imgs_list = [(img, img.get('alt')) for img in parse_html.find_all('img')]
    no_alt_list = []
    for img in imgs_list:
        if img[1] == None:
            no_alt_list.append((img[0].get('src')))
    return no_alt_list

# alt属性が記述されていないものを出力
def alt_not_written(parse_html):
    no_alt_list = [(img.get('src'), img.get('alt')) for img in parse_html.find_all('img') if img.get('alt') =='']
    return no_alt_list