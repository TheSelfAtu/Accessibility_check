import io
import re
import requests
import pytesseract

from PIL import Image
from tesserocr import PyTessBaseAPI, PSM

def ocr_text_on_image(imageURL):
    response = requests.get(imageURL)
    # print( type(response) ) # <class 'requests.models.Response'>
    img = Image.open(io.BytesIO(response.content))
    # print( type(img) ) # <class 'PIL.JpegImagePlugin.JpegImageFile'>
    text = pytesseract.image_to_string(img, lang='jpn')
    # print( text )
    text = re.sub('[\n\s]', '', text)
    # print(re.sub('[\n\s]', '', text))
 
    # print('len(text)', len(text),type(text))
    return text



# def ocrImage(imageURL):
#     api = PyTessBaseAPI(psm=PSM.AUTO, lang='jpn')
#     api.SetImageFile(imageURL)
#     print(api.GetUTF8Text())