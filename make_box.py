import pytesseract
import cv2
import PIL

capture_path = "C:/Users/Elite/Desktop/ocr/"
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

for i in range(1,113):
    img_path = capture_path + "test(" + str(i) + ").jpg"
    fp = open(img_path, "rb")
    img = PIL.Image.open(fp)
    txt = pytesseract.image_to_boxes(img, lang='lkr2')
    print("ocr 결과 : " + str(i) + txt)
    f = open('C:/Users/Elite/Desktop/ocr/test(' + str(i) + ').box', 'w')
    f.write(txt)
    f.close()