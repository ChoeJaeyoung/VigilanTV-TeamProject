from module.carplate import *
from module.color_identification import *
from module.extract_carplate_opencv import *
from module.filter_addIMG import *
from module.out_result import *
import os
import numpy as np
import cv2
import math
import imutils

num = 1
endnum = 5
f = open("img/ocr_result.txt", 'w')

while num <= endnum:
    inputCarDIR = 'img/car/car(' + str(num) + ').JPG'

    print("자동차사진 : " + str(num))
    # 자동차 색 판별################################################################################################
    carIMG = cv2.imread(inputCarDIR)
    identificator = colorIdentification(carIMG)
    color = identificator.color()
    print(color)
    #print(carIMG)


    # 자동차 번호판 자르기##########################################################################################
    detect = carplateDetecting(carIMG, 'cfg/obj.names', 'cfg/yolov2-carplate.cfg','cfg/yolov2-carplate_2200.weights')
    saveIMG = detect.parse()
    cv2.imwrite('img/plate/' + str(num) + '.jpg', saveIMG)


    # 번호판 이미지 전처리##########################################################################################
    inputFileName = 'img/plate/'+str(num)+'.jpg'
    outputFileName = 'img/result/'+str(num)+'.jpg'

    opencvIMG = extract_opencv(inputFileName, outputFileName)

    # 이미지 로드
    img_ori = cv2.imread(inputFileName, cv2.IMREAD_COLOR)

    # 이미지 확대
    img_ori = cv2.resize(img_ori, None, fx=4, fy=4, interpolation=cv2.INTER_LINEAR)
    height, width, channel = img_ori.shape
    print('height : ', height)
    print('width : ', width)

    # 이미지 전처리
    img = opencvIMG.img_preprocessing(img_ori)

    # 직선 검출, 직선 각도 검출
    degree = opencvIMG.detect_line(img)
    result = opencvIMG.img_rotate(img, degree, height, width)

    high_x = 0
    high_y = 0
    row_x = 0
    row_y = 0


    # 이미지 수축
    kernel2 = np.ones((3, 3), np.uint8)
    result = cv2.dilate(result, kernel2, iterations=1)

    img_ori2 = opencvIMG.img_rotate(img_ori, degree, height, width)

    result = opencvIMG.removeNoise(result)

    result2, high_y, high_x, row_y, row_x = opencvIMG.find_number(result, img_ori2, high_y, high_x, row_y, row_x, height, width)
    #cv2.imshow('img_ori', img_ori)
    #cv2.imshow('find_number', result2)

    result = opencvIMG.removeNoise(result[row_y: high_y, row_x: high_x])

    if result.any():
        img_ori_crop = img_ori2[row_y: high_y, row_x: high_x]


        print('이미지 받아왔나? ', result)
        print(type(result))

        result = cv2.resize(result, dsize=(432, 98), interpolation=cv2.INTER_LINEAR)

        cv2.imwrite(outputFileName, result)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


        # OCR ########################################################################################################
        ocr = out_result(outputFileName)
        resultOCR = ocr.output('52font+vkor')
        txt1 = str(num) + ' : ' + str(resultOCR) + '\n'
        print(txt1)

        f.write(txt1)

        num = num + 1
        print('------------------------------------------')

    else:
        print('실패 : ', num)
        txt2 = str(num) + ' : X\n'
        f.write(txt2)
        num = num + 1
        print('------------------------------------------')
        continue

f.close()


