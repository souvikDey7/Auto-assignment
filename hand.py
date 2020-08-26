# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 00:21:36 2020
#d:\anaconda\lib\site-packages
@author: deyso
"""
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\deyso\AppData\Local\Tesseract-OCR\tesseract.exe'
import opencv as cv
pic2=Image.open("pic2.jpg")
pic1=Image.open("pic1.jpg")
print("start")
e=cv.hconcat([pic2, pic1])
print(e)
#text=pytesseract.image_to_string(pic,lang="eng")
#for i in text:
#    print(i)
#print("done")
