import pytesseract
import cv2
import PIL

capture_path = "C:/Users/Elite/Desktop/makebox/test/"

#for i in range(48,57):
img_path = capture_path + "car" + str(1) + ".jpg"
fp = open(img_path, "rb")
img = PIL.Image.open(fp)
txt = pytesseract.image_to_boxes(img, lang='vkor')
print("ocr 결과 : " + str(1) + txt)
f = open('C:/Users/Elite/Desktop/makebox/car' + str(1) + '.box', 'w')
f.write(txt)
f.close()