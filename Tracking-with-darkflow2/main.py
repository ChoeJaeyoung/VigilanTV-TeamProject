# -*- coding: utf-8 -*-
from darkflow.darkflow.net.build import TFNet
import cv2
import numpy as np
from sort.sort import *
import time
from PIL import Image
import os
from flask import Flask, request, make_response
import json
import time
import PIL
import pytesseract
import os
import image
import PIL.Image

pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

timecheck = 0
point_list = []
count = 0
img_original = 0


options = {"model": "darkflow/cfg/yolo.cfg", "load": "darkflow/bin/yolo.weights", "threshold": 0.5}  # threshold가 신뢰율임
tfnet = TFNet(options)  # JSON

app = Flask(__name__)

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

#opencv 전처리 함수
def mouse_callback(event, x, y, flags, param):
    global point_list, count, img_original

    # 마우스 왼쪽 버튼 누를 때마다 좌표를 리스트에 저장
    if event == cv2.EVENT_LBUTTONDOWN:
        print("(%d, %d)" % (x, y))
        point_list.append((x, y))

        print(point_list)
        cv2.circle(img_original, (x, y), 1, (0, 255, 0), -1)

# 이미지 이진화
def threshold(img_result):
    plateIMG = img_result
    th2 = cv2.adaptiveThreshold(plateIMG,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,11,2)
    return th2

# 이미지 팽창
def dilate(img_result):
    plateIMG = img_result

    kernel2 = np.ones((2, 2), np.uint8)
    dilation2 = cv2.dilate(plateIMG, kernel2, iterations=1)

    return dilation2

# 이미지 침식
def erode(img_result):
    plateIMG = img_result

    kernel2 = np.ones((2, 2), np.uint8)
    dilation2 = cv2.erode(plateIMG, kernel2, iterations=1)

    return dilation2

# 이미지 샤프닝
def sharpen2(img_result):
    # Load source / input image as grayscale, also works on color images...
    imgIn = img_result

    # Create the identity filter, but with the 1 shifted to the right!
    kernel = np.zeros((9, 9), np.float32)
    kernel[4, 4] = 2.0  # Identity, times two!

    # Create a box filter:
    boxFilter = np.ones((9, 9), np.float32) / 81.0

    # Subtract the two:
    kernel = kernel - boxFilter

    # Note that we are subject to overflow and underflow here...but I believe that
    # filter2D clips top and bottom ranges on the output, plus you'd need a
    # very bright or very dark pixel surrounded by the opposite type.

    custom = cv2.filter2D(imgIn, -1, kernel)
    return custom

# 이미지 블러처리
def blur(img_result):
    # Load source / input image as grayscale, also works on color images...
    imgIn = img_result

    result = cv2.bilateralFilter(imgIn, 8, 40, 40)
    return result

# 이미지 샤프닝2
def sharpen(img_result):
    kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],[-1,2,2,2,-1],[-1,2,8,2,-1],[-1,2,2,2,-1],[-1,-1,-1,-1,-1]])/8.0 #정규화위해 8로나눔

    #applying different kernels to the input image
    output_3 = cv2.filter2D(img_result,-1,kernel_sharpen_3)

    #cv2.imshow('sh3-Edge Enhancement',output_3)

    return output_3

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

    img_big = cv2.resize(img_big, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

    return img_big

saveTrackerCrop = ""
@app.route('/getPath', methods = ['POST', 'GET'])
def getPath():
    print("Success connected")
    if request.method == 'POST':

        capture_path = "C:/Users/Elite/Desktop/capture/"

        json_path = request.get_json()
        path = json_path['serverPath']
        saveFileName = json_path['saveFileName']
        print(json_path['serverPath'])
        print(json_path['saveFileName'])
        #############################################################################################################
        # 주영tracker - detection
        cap = cv2.VideoCapture(path + saveFileName)  # 불러오는 파일 경로 및 이름
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
        output_avi = 'output.avi'

        # 파일 stream 생성
        out = cv2.VideoWriter(capture_path + output_avi, fourcc, fps, (int(width), int(height)))
        # output_avi : 파일 이름
        # fourcc : 코덱
        # fps : 초당 프레임 수
        # width : 넓이
        # height : 높이

        #################################
        IDcount = {}
        XYbox = {}
        print("IDcount_first : ")
        print(IDcount)
        print("XYbox_first : ")
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
                    if IDcount[strID] == 45:
                        XYbox[strID + "3s"] = [1, trackers_id[i][0], trackers_id[i][1], trackers_id[i][2],
                                              trackers_id[i][3]]
                        print("XYbox 90프레임 때 캡쳐 된 좌표 추가 : ")
                        print(XYbox)
                        xy = XYbox[strID + "3s"]
                        topx = xy[1]
                        topy = xy[2]
                        bottomx = xy[3]
                        bottomy = xy[4]
                        # saveEvidence = "img_id" + strID + "_3s" + ".jpg"
                        #saveEvidenceCrop = "box_id" + strID + "_3s" + ".jpg"
                        cv2.imwrite(capture_path + "img_id" + strID + "_3s" + ".jpg", tracking)
                        cropped = frame[int(topy):int(bottomy) + 1, int(topx):int(bottomx) + 1]
                        cv2.imwrite(capture_path + "box_id" + strID + "_3s" + ".jpg", cropped)
                        print(capture_path + "box_id" + strID + "_3s" + ".jpg")

                    # 300 프레임(10초) 넘어가는 애들 증거 사진 촬영 (이미지 저장)
                    if IDcount[strID] == 80:
                        XYbox[strID + "5s"] = [2, trackers_id[i][0], trackers_id[i][1], trackers_id[i][2], trackers_id[i][3]]
                        print("XYbox 150프레임(5초) 때 캡쳐 된 좌표 추가 : ")
                        print(XYbox)
                        xy = XYbox[strID + "5s"]
                        topx = xy[1]
                        topy = xy[2]
                        bottomx = xy[3]
                        bottomy = xy[4]
                        saveEvidenceCrop = "img_id" + strID + "_5s" + ".jpg"
                        saveTrackerCrop = "box_id" + strID + "_5s" + ".jpg"
                        cv2.imwrite(capture_path + "img_id" + strID + "_5s" + ".jpg", tracking)
                        cropped = frame[int(topy):int(bottomy) + 1, int(topx):int(bottomx) + 1]
                        cv2.imwrite(capture_path + "box_id" + strID + "_5s" + ".jpg", cropped)
                        print(capture_path + "box_id" + strID + "_5s" + ".jpg")

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
            if fps >= 60:  # 150 (5초 일 때)
                print("ID : " + id + "는 불법 주정차 차량입니다.")
                print("사각형 좌표 : ")

        print("IDcount : ")
        print(IDcount)

        print("XYbox : ")
        print(XYbox)

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

        # print(point)
        # print(trackers_id)
        ###############################################################################################################


        #############################################################################################################
        #지현 OpenCV 전처리

        # 원본 이미지
        global img_original
        img_original = cv2.imread(capture_path + saveTrackerCrop, cv2.IMREAD_GRAYSCALE)

        cv2.namedWindow(capture_path+saveTrackerCrop)
        cv2.setMouseCallback(capture_path+saveTrackerCrop, mouse_callback)
        print("path:",capture_path+saveTrackerCrop)

        while (True):
            # img_original = cv2.resize(img_original, (1200, 900))
            cv2.imshow(capture_path+saveTrackerCrop, img_original)

            # height, weight = img_original.shape[:2]
            # 수정하지 말것
            height = 49
            weight = 216

            if cv2.waitKey(1) & 0xFF == 32:  # spacebar를 누르면 루프에서 빠져나옵니다.
                break

        # 좌표 순서 - 상단왼쪽 끝, 상단오른쪽 끝, 하단왼쪽 끝, 하단오른쪽 끝
        print('point_list[0]', point_list[0])
        print('point_list[1]', point_list[1])
        print('point_list[2]', point_list[2])
        print('point_list[3]', point_list[3])
        pts1 = np.float32([list(point_list[0]), list(point_list[1]), list(point_list[2]), list(point_list[3])])
        #print("pts1 : " + pts1)
        pts2 = np.float32([[0, 0], [weight, 0], [0, height], [weight, height]])

        print(pts1)
        print(pts2)

        m = cv2.getPerspectiveTransform(pts1, pts2)
        img_result = cv2.warpPerspective(img_original, m, (weight, height))
        # img_result : 왜곡보정된 이미지

        # Image Filtering
        img_result = sharpen(img_result)
        img_result = blur(img_result)
        img_result = threshold(img_result)
        img_result = dilate(img_result)

        # cv2.imshow('img_result', img_result)
        # cv2.imshow('img_original', img_original)

        # Remove Noise
        img_result2 = removeNoise(img_result)
        # cv2.imshow('img_result2', img_result2)
        now = time.gmtime(time.time())

        final_save = str(now.tm_mon) + str(now.tm_mday) + str(now.tm_hour) + str(now.tm_min) + str(now.tm_sec) + "_final.jpg"
        cv2.imwrite(capture_path + final_save, img_result2)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        ##############################################################################################################

        img_path = capture_path + "realtest.jpg"

        fp = open(img_path, "rb")
        img = PIL.Image.open(fp)

        txt = pytesseract.image_to_string(img, lang='kor2')
        print("ocr 결과 : " + txt)

        ############################################################################################################
        # response
        data = {"capture_path":capture_path, "saveEvidenceCrop":saveEvidenceCrop, "saveTrackerCrop":saveTrackerCrop, "final_save":final_save, "txt":txt}
        path_data = json.dumps(data)
        print(path_data)
        response = make_response(path_data)
        response.headers['Content-Type'] = 'application/json'
        print(str(response))
        return response

if __name__ == '__main__':
    app.run(debug=True, host='localhost')

