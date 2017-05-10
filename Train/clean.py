import cv2
import os
import numpy as np

files = os.listdir("Stock")

for file in files:
	img = cv2.imread("Stock/"+file, 0)
	median = cv2.medianBlur(img ,5)	
	dst = cv2.fastNlMeansDenoising(median,None,30,7,21)
	laplacian = cv2.Laplacian(dst,cv2.CV_64F)
	ret,thresh2 = cv2.threshold(laplacian,2,255,cv2.THRESH_BINARY)
	# sobelx = cv2.Sobel(dst,cv2.CV_64F,1,0,ksize=5)
	# edges = cv2.Canny(laplacian,100,200)
	# img = cv2.cvtColor(sobelx, cv2.COLOR_BGR2GRAY)
	cv2.imwrite("Temp/"+file, thresh2)
