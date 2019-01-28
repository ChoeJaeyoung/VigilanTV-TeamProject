import cv2
import numpy
from matplotlib import pyplot as plt

# 이미지 필터
image = cv2.imread('image/test2/c1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8,8))
img2 = clahe.apply(gray)
cv2.imwrite('image/test2/c1_filter.jpg', img2) # ccc가 필터 씌워진 애

###########################################################################
# 이미지 합성
img1 = cv2.imread('image/test2/c1.jpg')  # 원본 애
img2 = cv2.imread('image/test2/c1_filter.jpg') # 필터 씌운애
cv2.imshow('1', img1)
cv2.imshow('2', img2)

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 170, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask = mask)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2, img2, mask = mask_inv)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst
cv2.imshow('result', img1)
cv2.imwrite('image/test2/c1_addResult.jpg', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()