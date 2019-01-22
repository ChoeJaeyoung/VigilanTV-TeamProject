# -*- coding: utf-8 -*-
import numpy as np
import cv2

point_list = []
count = 0

def mouse_callback(event, x, y, flags, param):
    global point_list, count, img_original


    # 마우스 왼쪽 버튼 누를 때마다 좌표를 리스트에 저장
    if event == cv2.EVENT_LBUTTONDOWN:
        print("(%d, %d)" % (x, y))
        point_list.append((x, y))

        print(point_list)
        cv2.circle(img_original, (x, y), 1, (0, 255, 0), -1)

# 이미지 노이즈 처리
def removeNoise(img_result):
    img = img_result
    #cv2.imshow('original', img)

    img_big = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    copy_img = img_big.copy()

    img_blur = cv2.bilateralFilter(img_big, 8, 10, 10)
    #cv2.imshow('gray', img_blur)

    img_edge2 = cv2.Canny(img_big, 100, 300, 3)
    #cv2.imshow('Canny', img_edge2)

    cnt, contours, hierarchy = cv2.findContours(img_edge2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    box_point = []
    f_count = 0
    select = 0
    plate_width = 0

    for i in range(len(contours)):
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        x, y, w, h = cv2.boundingRect(cnt)
        rect_area = w * h
        aspect_ratio = float(w) / h
        aspect_ratio2 = float(h) / w

        # if (aspect_ratio>=0.2)and(aspect_ratio<=2.0)and(rect_area>=100)and(rect_area<=700):
        if (aspect_ratio2 >= 0.5) and (h > 30):
            # cv2.rectangle(img_big, (x, y), (x+w, y+h), (0, 255, 0), 1)
            # box_point.append(cv2.boundingRect(cnt))
            continue;
        else:
            cv2.rectangle(img_big, (x, y), (x + w, y + h), (255, 255, 255), -10)

    img_big = cv2.resize(img_big, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_CUBIC)

    return img_big


def threshold_train(img_result):
    plateIMG = img_result

    plateIMG = cv2.bilateralFilter(plateIMG, 9, 40, 40)
    #cv2.imshow('bilateral', plateIMG)

    th2 = cv2.adaptiveThreshold(plateIMG,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,11,2)

    #cv2.imshow('Adaptive Mean Thresholding', th2 )

    kernel = np.ones((1, 1), np.uint8)
    dilation1 = cv2.erode(th2, kernel, iterations=1)

    #cv2.imshow('Mean', dilation1)
    return dilation1


for input in range(1,34):
    inputfileName = 'car/IMG_(' + str(input) + ').jpg'
    resultfileName = 'resultCar/result_' + str(input) + '.JPG'
    print(inputfileName)

    cv2.namedWindow(inputfileName)
    cv2.setMouseCallback(inputfileName, mouse_callback)

    # 원본 이미지
    img_original = cv2.imread(inputfileName, cv2.IMREAD_GRAYSCALE)

    while(True):
        #img_original = cv2.resize(img_original, (1200, 900))
        cv2.imshow(inputfileName, img_original)

        #height, weight = img_original.shape[:2]
        #수정하지 말것
        height=49
        weight=216

        if cv2.waitKey(1)&0xFF == 32: # spacebar를 누르면 루프에서 빠져나옵니다.
            break

    # 좌표 순서 - 상단왼쪽 끝, 상단오른쪽 끝, 하단왼쪽 끝, 하단오른쪽 끝
    pts1 = np.float32([list(point_list[0]),list(point_list[1]),list(point_list[2]),list(point_list[3])])
    pts2 = np.float32([[0,0],[weight,0],[0,height],[weight,height]])

    print(pts1)
    print(pts2)

    M = cv2.getPerspectiveTransform(pts1,pts2)
    img_result = cv2.warpPerspective(img_original, M, (weight,height))
    #img_result : 왜곡보정된 이미지



    img_result = threshold_train(img_result)


    # Remove Noise
    img_result2 = removeNoise(img_result)
    cv2.imshow('img_result2', img_result2)
    cv2.imwrite(resultfileName, img_result2)
    pts1 = np.zeros(shape=0)
    pts2 = np.zeros(shape=0)

    point_list = [ ]
    cv2.waitKey(0)
    cv2.destroyAllWindows()