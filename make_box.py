import pytesseract
import cv2
import PIL

capture_path = "C:/Users/Elite/Desktop/testOCR/plate2/"

for i in range(1,54):
    img_path = capture_path + "img_(" + str(i) + ").jpg"
    fp = open(img_path, "rb")
    img = PIL.Image.open(fp)
    txt = pytesseract.image_to_boxes(img, lang='kor2')
    print("ocr 결과 : " + str(i) + txt)
    f = open('C:/Users/Elite/Desktop/testOCR/img_(' + str(i) + ').box', 'w')
    f.write(txt)
    f.close()