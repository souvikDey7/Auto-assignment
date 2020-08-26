# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 00:21:36 2020
#d:\anaconda\lib\site-packages
@author: deyso
"""

from PIL import Image
import pytesseract
#pytesseract.pytesseract.tesseract_cmd="D:\Anaconda\Lib\site-packages\pytesseract"
pic=Image.open("pic.jpg")
text=pytesseract.image_to_string(pic)
print(text)