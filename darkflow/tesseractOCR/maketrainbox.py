# -*- coding: utf-8 -*-
import pytesseract
import PIL
import pandas as pd

capture_path = "C:/Users/Elite/Desktop/dpi/"


for i in range(1,391):
    #img파일
    img_path = capture_path + "exam (" + str(i) + ").jpg"
    fp = open(img_path, "rb")
    img = PIL.Image.open(fp)
    #make_box
    txt = pytesseract.image_to_boxes(img, lang="52font+50kor")
    print("ocr 결과 : " + txt)
    print('index' + str(i))
    f = open(capture_path + 'exam ('+ str(i) + ').box', 'w', encoding='utf-8')
    f.write(txt+ '\n')

f.close()