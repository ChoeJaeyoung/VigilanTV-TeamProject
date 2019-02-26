# -*- coding: utf-8 -*-
import pytesseract
import PIL
import pandas as pd

capture_path = "C:/Users/Elite/Desktop/"


for i in range(2,3):
    #img파일
    img_path = capture_path + "test" + str(i) + ".jpg"
    fp = open(img_path, "rb")
    img = PIL.Image.open(fp)
    #박스 생성하기
    txt = pytesseract.image_to_boxes(img, lang="1499lstm2+52font")
    print("ocr 결과 : " + txt)
    print('index' + str(i))
    f = open(capture_path + 'second ('+ str(i) + ').box', 'w', encoding='utf-8')
    f.write(txt+ '\n')

f.close()