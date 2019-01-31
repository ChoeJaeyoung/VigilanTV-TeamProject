from darkflow.net.build import TFNet
import cv2
import numpy as np
from sort.sort import *
import time
from PIL import Image
import os

timecheck = 0

options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.5}  # threshold가 신뢰율임
tfnet = TFNet(options)  # JSON


# 사실상 얘는 안쓰는 함수임
def boxing(original_img, predictions):
    newImage = np.copy(original_img)

    for result in predictions:
        if result['label'] != 'car':
            continue
        top_x = result['topleft']['x']
        top_y = result['topleft']['y']

        btm_x = result['bottomright']['x']
        btm_y = result['bottomright']['y']

        confidence = result['confidence']
        label = result['label'] + " " + str(round(confidence, 3))

        if confidence > 0.25:
            newImage = cv2.rectangle(newImage, (top_x, top_y), (btm_x, btm_y), (255, 0, 0), 3)
            newImage = cv2.putText(newImage, label, (top_x, top_y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8,
                                   (0, 230, 0), 1, cv2.LINE_AA)

    return newImage


# 얘 쓰는 함수임
def getPoint(predictions):
    bboxes = []
    for result in predictions:
        if result['label'] != 'car':
            continue
        top_x = result['topleft']['x']
        top_y = result['topleft']['y']

        btm_x = result['bottomright']['x']
        btm_y = result['bottomright']['y']

        score = result['confidence']  # 신뢰율

        bbox = [top_x, top_y, btm_x, btm_y, score]  # 5개까지만 sort가 읽음
        bboxes.append(bbox)

    bboxes = np.array(bboxes)  # sort 적용하려면 numpy array로 넣어줘야함 (5개)

    return bboxes


def id_box(image, boxes):
    image = np.copy(image)

    for box in boxes:
        top_x = int(box[0])
        top_y = int(box[1])
        btm_x = int(box[2])
        btm_y = int(box[3])

        track_id = str(int(box[4]))

        image = cv2.rectangle(image, (top_x, top_y), (btm_x, btm_y), (255, 255, 255), 3)
        image = cv2.putText(image, track_id, (top_x, top_y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255, 255, 255),1)

    return image


cap = cv2.VideoCapture('test03.MOV')
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
        results = tfnet.return_predict(frame)  # JSON
        dets = getPoint(results)
        trackers_id = tracker.update(dets)
        tracking = id_box(frame, trackers_id)

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
                cv2.imwrite("output/img_id" + strID + "_3s" + ".jpg", tracking)
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

# 불법 주정차 차량 판단하기#####################################
for id, fps in IDcount.items():
    if fps >= 150:  # 150 (5초 이상 일때)
        print("ID : " + id + "는 불법 주정차 차량입니다.")
        print("사각형 좌표 : ")
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
