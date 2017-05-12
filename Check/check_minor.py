import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("test.png", 0)
median = cv2.medianBlur(img ,5)	
dst = cv2.fastNlMeansDenoising(median,None,10,7,21)
ret,thresh2 = cv2.threshold(dst,230,255,cv2.THRESH_BINARY)


maxes = []
name = []

dirs = os.listdir("Test")


# All the 6 methods for comparison in a list
methods = 'cv2.TM_CCOEFF_NORMED'


template1 = cv2.imread("Test/3.png",0)
template2 = cv2.imread("Test/S.png",0)

method = eval(methods)
# cv2.imwrite("thresh.jpg", thresh2)
# thresh2 = cv2.imread("thresh.jpg")
res = cv2.matchTemplate(thresh2,template1,method)
res = res*255
print(res.shape)
cv2.imwrite("element.jpg",res)

# print(maxes)
# print(name)