import cv2
import os
import numpy as np

files = os.listdir("Stock")

for file in files:
	img = cv2.imread("Stock/"+file, 0)
	median = cv2.medianBlur(img ,5)	
	dst = cv2.fastNlMeansDenoising(median,None,10,7,21)
	ret,thresh2 = cv2.threshold(dst,230,255,cv2.THRESH_BINARY)
	# laplacian = cv2.Laplacian(dst,cv2.CV_64F)
	# sobelx = cv2.Sobel(dst,cv2.CV_64F,1,0,ksize=5)
	# edges = cv2.Canny(laplacian,100,200)
	cv2.imwrite("Temp/"+file, thresh2)
