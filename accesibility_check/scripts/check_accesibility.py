import requests
from .ocr import * 
from bs4 import BeautifulSoup

# HTMLのパース
def parse_html(url):
    # HTML全体を表示する
    parse_url = requests.get(url)
    soup = BeautifulSoup(parse_url.text, 'html.parser')
    return soup


# 画像中のテキストが多い場合そのimgの（src,文字数）を返す
def too_much_letters_on_image(parse_html):
    too_much_letters_list = []
    imgSrcList = [img.get('src') for img in parse_html.find_all('img')]
    for imgSrc in imgSrcList:
        len_letters = len(ocr_text_on_image(imgSrc))
        if len_letters > 20 :
            too_much_letters_list.append((imgSrc,'文字数：'+ str(len_letters)))
    return too_much_letters_list

# alt属性が存在しないタグをチェック
def alt_none(parse_html):
    imgs_list = [(img, img.get('alt')) for img in parse_html.find_all('img')]
    no_alt_list = []
    for img in imgs_list:
        if img[1] == None:
            no_alt_list.append((img[0].get('src')))
    return no_alt_list

# alt属性が空のもののリストを出力
def alt_not_written(parse_html):
    no_alt_list = [(img.get('src'), img.get('alt')) for img in parse_html.find_all('img') if img.get('alt') =='']
    return no_alt_list