import  cv2
import pytesseract
from pytesseract import Output
img = cv2.imread('receipt3.png', cv2.IMREAD_GRAYSCALE)
extracted_text = pytesseract.image_to_string(img, lang = 'eng')
d = pytesseract.image_to_data(img , output_type=Output.DICT)
n_boxes = len( d['level'])
for i in range(n_boxes):
    (x,y,w,h) = ( d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    img = cv2.rectangle(img, (x,y), (x+w , y+h), (0,0, 255),2)
cv2.imshow( 'img', img)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("result : ",extracted_text)
cv2.waitKey(0)