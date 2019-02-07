from module.carplate import *
from module.color_identification import *
from module.extract_carplate_opencv import *
#from module.filter_addIMG import *
from module.out_result import *
#from module.main import *
import os
import numpy as np
import cv2
import math
import imutils
from darkflow.net.build import TFNet
from sort.sort import *
import time
from PIL import Image
import os


###################################################################################################################################
videotrack = traker()
cap = cv2.VideoCapture('img/test03.MOV')
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
tracker = Sort()
totalFrame = 0
# 재생할 파일의 넓이 얻기
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# 재생할 파일의 높이 얻기
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# 재생할 파일의 프레임 레이트 얻기
fps = cap.get(cv2.CAP_PROP_FPS)

# XVID가 제일 낫다고 함.
# linux 계열 DIVX, XVID, MJPG, X264, WMV1, WMV2.
# windows 계열 DIVX
# 저장할 비디오 코덱
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# 저장할 파일 이름
filename = 'output/output.avi'

# 파일 stream 생성
out = cv2.VideoWriter(filename, fourcc, fps, (int(width), int(height)))
# filename : 파일 이름
# fourcc : 코덱
# fps : 초당 프레임 수
# width : 넓이
# height : 높이

#################################
IDcount = {}
XYbox = {}
print("IDcount : ")
print(IDcount)
print("XYbox : ")
print(XYbox)
################################
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:
        (H, W) = frame.shape[:2]
        # matrix = cv2.getRotationMatrix2D((W/2, H/2), 270, 1)
        # frame = cv2.warpAffine(frame, matrix, None)

        frame = np.asarray(frame)
        results = videotrack.tfnet.return_predict(frame)  # JSON
        dets = videotrack.getPoint(results)
        trackers_id = tracker.update(dets)
        tracking = videotrack.id_box(frame, trackers_id)

        # ID 별로 frame 수 카운트
        num = len(trackers_id)
        for i in range(num):
            print(trackers_id[i][4])
            strID = str(trackers_id[i][4])
            if strID in IDcount.keys():
                IDcount[strID] += 1
            else:
                IDcount[strID] = 1

            # 90 프레임 (3초) 넘어가는 애들은 첫 사진 촬영 (이미지 저장)
            if IDcount[strID] == 150:
                XYbox[strID + "3s"] = [1, trackers_id[i][0], trackers_id[i][1], trackers_id[i][2], trackers_id[i][3]]
                print("XYbox 90프레임 때 캡쳐 된 좌표 추가 : ")
                print(XYbox)
                xy = XYbox[strID + "3s"]
                topx = xy[1]
                topy = xy[2]
                bottomx = xy[3]
                bottomy = xy[4]
                cv2.imwrite("ouput/img_id" + strID + "_3s" + ".jpg", tracking)
                cropped = frame[int(topy):int(bottomy) + 1, int(topx):int(bottomx) + 1]
                cv2.imwrite("output/box_id" + strID + "_3s" + ".jpg", cropped)

            # 300 프레임(10초) 넘어가는 애들 증거 사진 촬영 (이미지 저장)
            if IDcount[strID] == 300:
                XYbox[strID + "5s"] = [2, trackers_id[i][0], trackers_id[i][1], trackers_id[i][2], trackers_id[i][3]]
                print("XYbox 150프레임(5초) 때 캡쳐 된 좌표 추가 : ")
                print(XYbox)
                xy = XYbox[strID + "5s"]
                topx = xy[1]
                topy = xy[2]
                bottomx = xy[3]
                bottomy = xy[4]
                cv2.imwrite("output/img_id" + strID + "_5s" + ".jpg", tracking)
                cropped = frame[int(topy):int(bottomy) + 1, int(topx):int(bottomx) + 1]
                cv2.imwrite("output/box_id" + strID + "_5s" + ".jpg", cropped)

        totalFrame = totalFrame + 1

        # Display the resulting frame
        cv2.imshow('frame', tracking)
        # print(totalFrame)
        out.write(tracking)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

total = 0
idlist = []
# 불법 주정차 차량 판단하기#####################################
for id, fps in IDcount.items():
    if fps >= 150:  # 150 (5초 이상 일때)
        print("ID : " + id + "는 불법 주정차 차량입니다.")
        print("사각형 좌표 : ")
        total = total + 1
        idlist.append(id)
###########################################################

print("IDcount : ")
print(IDcount)

print("XYbox : ")
print(XYbox)


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# print(point)
# print(trackers_id)
###################################################################################################################################
num = 0
endnum = total
#idlist[num]
f = open("img/ocr_result.txt", 'w')

while num <= endnum:
    inputCarDIR = 'output/box_id' + str(idlist[num]) + '_5s.jpg'

    print("자동차사진 : " + str(idlist[num]))
    # 자동차 색 판별################################################################################################
    carIMG = cv2.imread(inputCarDIR)
    identificator = colorIdentification(carIMG)
    color = identificator.color()
    print(color)
    #print(carIMG)


    # 자동차 번호판 자르기##########################################################################################
    detect = carplateDetecting(carIMG, 'cfg/obj.names', 'cfg/yolov2-carplate.cfg','cfg/yolov2-carplate_2200.weights')
    saveIMG = detect.parse()
    cv2.imwrite('img/plate/' + str(idlist[num]) + '.jpg', saveIMG)


    # 번호판 이미지 전처리##########################################################################################
    inputFileName = 'img/plate/'+str(idlist[num])+'.jpg'
    outputFileName = 'img/result/'+str(idlist[num])+'.jpg'

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
    # cv2.imshow('final_result', result)

    if result.any():
        print('이미지 받아왔나? ', result)
        print(type(result))

        result = cv2.resize(result, dsize=(432, 98), interpolation=cv2.INTER_LINEAR)

        cv2.imwrite(outputFileName, result)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # OCR ########################################################################################################
        ocr = out_result(outputFileName)
        resultOCR = ocr.output('52font+vkor')
        txt1 = str(idlist[num]) + ' : ' + str(resultOCR) + '\n'
        print(txt1)

        f.write(txt1)

        num = num + 1
        print('------------------------------------------')

    else:
        print('실패 : ', idlist[num])
        txt2 = str(idlist[num]) + ' : X\n'
        f.write(txt2)
        num = num + 1
        print('------------------------------------------')
        continue

f.close()


