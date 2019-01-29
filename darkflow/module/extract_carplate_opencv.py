# -*- coding: utf-8 -*-
import numpy as np
import cv2
import math
import imutils

noise = 0

def removeNoise(img_edge2):
    img = img_edge2

    cnt, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    box_point = []
    f_count = 0
    select = 0
    plate_width = 0

    global height, width
    for i in range(len(contours)):
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        x, y, w, h = cv2.boundingRect(cnt)
        rect_area = w * h
        aspect_ratio = float(w) / h
        aspect_ratio2 = float(h) / w

        if (aspect_ratio2 >= 0.3) and (h > (height*0.2)):
            #cv2.rectangle(img_big, (x, y), (x+w, y+h), (0, 255, 0), 1)
            #box_point.append(cv2.boundingRect(cnt))
            continue;
        elif (w < width*0.8):
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), -1)
            continue;
    cv2.imshow('remove_noise', img)

    return img

def img_preprocessing(img):
    # 이미지 로드
    img_original = img

    # 이미지 흑백화
    img_original = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)

    imgray = cv2.bilateralFilter(img_original, 8, 50, 50)
    cv2.imshow('blur', imgray)

    # 이미지 수축
    kernel2 = np.ones((3, 3), np.uint8)
    imgray = cv2.dilate(imgray, kernel2, iterations=1)

    #img_edge2 = cv2.Canny(img, 100, 300, 3)
    # cv2.imshow('Canny', img_edge2)

    # 이미지 흑백화
    #imgray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)

    #imgray = cv2.equalizeHist(imgray)
    imgray = cv2.bilateralFilter(imgray, 10, 120, 120)
    cv2.imshow('equalizeHist', imgray)

    # 이미지 이진화
    imgray = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)

    # 이미지 팽창
    kernel = np.ones((5, 5), np.uint8)
    imgray = cv2.erode(imgray, kernel, iterations=1)

    # 노이즈 제거
    #imgray = removeNoise(imgray)
    global noise
    noise = imgray

    # 이미지 윤곽선 따기
    img_edge = cv2.Canny(imgray, 50, 100, 3)

    cv2.imshow('img_preprocessing', img_edge)

    return img_edge

def detect_line(img):
    lines = cv2.HoughLines(img, 1, np.pi / 180, 50)

    if lines is None:
        print("Do not Detect Lines")
        return -90;
    else:
        for rho, theta in lines[0]:
            x1 = int(np.cos(theta) * rho + 1000 * (-np.sin(theta)))
            y1 = int(np.sin(theta) * rho + 1000 * np.cos(theta))
            x2 = int(np.cos(theta) * rho - 1000 * (-np.sin(theta)))
            y2 = int(np.sin(theta) * rho - 1000 * np.cos(theta))
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)


            rad = math.atan2(x1 - x2, y1 - y2)
            angle = (rad * 180) / np.pi
            print(angle)

        #cv2.imshow('result', img)

        return angle

def img_rotate(img, degree):
    #\height, width = img.shape
    #matrix = cv2.getRotationMatrix2D((width / 2, height / 2), -(degree + 90), 1)
    #dst = cv2.warpAffine(img, matrix, (width, height))

    dst = imutils.rotate_bound(img, (degree + 90))

    return dst
















# 이미지 로드

img_number = '2'
inputFileName = 'realdata2/'+img_number+'.jpg'
outputFileName = 'realoutput2/'+img_number+'.jpg'
img_original = cv2.imread(inputFileName, cv2.IMREAD_COLOR)

hist_full = cv2.calcHist([img_original],[1],None,[256],[0,256])
print("histogram", hist_full)
# 이미지 확대
img_original = cv2.resize(img_original, None, fx=4, fy=4, interpolation=cv2.INTER_LINEAR)
height, width, channel = img_original.shape

print('height', height)
print('width', width)


# 이미지 전처리
img = img_preprocessing(img_original)
# 직선 검출, 직선 각도 검출
degree = detect_line(img)
result = img_rotate(noise, degree)

cv2.imshow('rotate', result)

high_x = 0
high_y = 0
row_x = 0
row_y = 0


def find_number(img_edge2, img_original):
    global high_y, high_x, row_y, row_x
    img = img_edge2
    # cv2.imshow('original', img)

    #img_big = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
    img_big = img.copy()

    img_blur = cv2.bilateralFilter(img_big, 8, 10, 10)
    # cv2.imshow('gray', img_blur)

    img_edge2 = cv2.Canny(img_big, 100, 300, 3)
    # cv2.imshow('Canny', img_edge2)

    cnt, contours, hierarchy = cv2.findContours(img_edge2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    box_point = []
    f_count = 0
    select = 0
    plate_width = 0

    first = 0
    for i in range(len(contours)):
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        x, y, w, h = cv2.boundingRect(cnt)
        rect_area = w * h
        aspect_ratio = float(w) / h
        aspect_ratio2 = float(h) / w

        global height, width
        # if (aspect_ratio>=0.2)and(aspect_ratio<=2.0)and(rect_area>=100)and(rect_area<=700):
        if (aspect_ratio2 >= 0.3) and (h > (height*0.3)) and (w < (width*0.2)) and (w > (width*0.04)):
            #cv2.rectangle(img_original, (x, y), (x + w, y + h), (0, 255, 0), 1)
            if (first == 0):
                row_x = x
                row_y = y
                first = 1

            if (x + w > high_x):
                high_x = x + w
            if (x < row_x):
                row_x = x
            if (y + h > high_y):
                high_y = y + h
            if (y < row_y):
                row_y = y

            continue;
        else:
            #cv2.rectangle(img_original, (x, y), (x + w, y + h), (100, 100, 100), 1)
            continue;

    #cv2.rectangle(img_original, (row_x, row_y), (high_x, high_y), (0, 255, 0), 1)
    box_point.append(cv2.boundingRect(cnt))

    img_big = cv2.resize(img_big, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)

    return img_original


img_original2 = img_rotate(img_original, degree)
result2 = find_number(result, img_original2)
cv2.imshow('img_original', img_original)
cv2.imshow('find_number', result2)

cv2.imwrite(outputFileName, result2[row_y-2: high_y+2, row_x-2: high_x+2])

cv2.waitKey(0)
cv2.destroyAllWindows()