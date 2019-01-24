import cv2
import numpy as np
import imutils

# 객체를 만들 때 클래스(colorIdentification())를 호출하면서 opencv로 읽어들인 이미지 객체명을 입력함.
# color라는 함수는 사진 속 물체의 색상을 리턴함.
# 현재 빨강, 초록, 파랑, 검은색, 하얀색/회색을 지원함.

def colorEqualize(image):
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(image_hsv)
    V_eq = cv2.equalizeHist(V)
    image_hsv_eq = cv2.merge((H, S, V_eq))
    image_bgr_modified = cv2.cvtColor(image_hsv_eq, cv2.COLOR_HSV2BGR)
    return image_bgr_modified

def colorCluster(image, cluster = 10):
    Z = image.reshape((-1, 3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, label, center = cv2.kmeans(Z, cluster, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    image_clustered = res.reshape((image.shape))
    return image_clustered

def foreMask(image):
    mask = np.zeros(image.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    rect = (50,50,450,290)
    cv2.grabCut(image,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    image_masked = image*mask2[:,:,np.newaxis]
    return image_masked

def crop(image):
    H, W = image.shape[:2]
    image_crop = image[int(H/6):5*int(H/6),int(W/6):5*int(W/6)]
    image_crop = cv2.resize(image_crop,(300,300))
    return image_crop

class colorIdentification():
    def __init__(self, image):
        self.image = image

    def color(self):
        image = self.image
        image = imutils.resize(image, height=300)

        image_equalized = colorEqualize(image)
        image_blur = cv2.bilateralFilter(image_equalized, 100, 50, 50)
        # image_eq_clustered = colorCluster(image_blur)
        image_eq_zoom = crop(image_blur)

        image_hsv = cv2.cvtColor(image_eq_zoom, cv2.COLOR_BGR2HSV)

        color_list = {'red1': [0, 255, 255],
                      'red2': [180, 255, 255],
                      'green': [60, 255, 255],
                      'blue': [120, 255, 255],
                      'yellow': [30, 255, 255],
                      'orange': [12, 255, 255],
                      'black': [0, 0, 0],
                      'white_or_gray': [0, 0, 255]}

        color_count = {'red': 0,
                       'red1': 0,
                       'red2': 0,
                       'green': 0,
                       'blue': 0,
                       'yellow': 0,
                       'orange': 0,
                       'black': 0,
                       'white_or_gray': 0}

        for i in list(color_list):
            if i == 'red1' or 'red2' or 'green' or 'blue' or 'yellow' or 'orange':
                lower_color = (color_list[i][0] - 10, color_list[i][1] - 222, color_list[i][2] - 210)
                upper_color = (color_list[i][0] + 10, color_list[i][1], color_list[i][2])

            if i == 'black':
                lower_color = (0, 0, 1)
                upper_color = (255, 100, 110)

            if i == 'white_or_gray':
                lower_color = (0, 0, 110)
                upper_color = (255, 40, 255)

            img_mask = cv2.inRange(image_hsv, lower_color, upper_color)
            img_result = cv2.bitwise_and(image_eq_zoom, image_eq_zoom, mask=img_mask)

            array_a = img_mask.reshape((-1, 3))
            list_a = [list(array_a[j]) for j in range(len(array_a))]
            num_a = [sum(list_a[k]) for k in range(len(list_a))]
            color_count[i] = 30000 - num_a.count(0)

        color_count['red'] = color_count['red1'] + color_count['red2']

        car_color = max(color_count.items(), key=lambda x: x[1])[0]

        return car_color

image1 = cv2.imread('car15.jpg')
identificator = colorIdentification(image1)
color = identificator.color()
print(color)