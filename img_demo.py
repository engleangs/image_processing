import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("receipt.png",0)
ret,thresh1 = cv2.threshold( img , 210,255, cv2.THRESH_BINARY)
cv2.imshow( 'gray',thresh1)