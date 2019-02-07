# -*- coding: utf-8 -*-
import pytesseract
import PIL
import pandas as pd

capture_path = "C:/Users/Elite/Desktop/makebox/test/"
all_words = 0
counts = 0
fail = []

for i in range(1,5):
    #box 불러오기
    df = pd.read_csv(capture_path + 'car' + str(i) +'.box', sep=' ', header=None)
    box_data = df[0].tolist()
    print(df)
    print(box_data)

    #img파일
    img_path = capture_path + "car" + str(i) + ".jpg"
    fp = open(img_path, "rb")
    img = PIL.Image.open(fp)
    #config setting
    config= ('-l 1024all+52font --oem 0 --psm 6')
    #ocr_result
    txt = pytesseract.image_to_string(img, config= config)
    all_words += 7
    txt = txt.replace(' ', '')
    try:
        for index in range(len(box_data)):
            if str(box_data[index]) != txt[index]:
                counts += 1
                fail.append(str(i))
                print('실패 : ' + str(i))
    except IndexError:
        txt = txt + 'a'
    #make_box
    #txt = pytesseract.image_to_boxes(img, lang="vikor2")
    print("ocr 결과 : " + txt)
    print('index' + str(i))
    f = open(capture_path + 'font_testkor' + '.txt', 'a')
    f.write(txt+ '\n')

print('총 단어의 수 :' + str(all_words))
print('틀린 단어 수 : ' + str(counts))
print('인식율 : ' + str(100 -(counts/all_words*100)))
for fa in fail:
    print("틀린 번호판 :" + fa)

f.close()