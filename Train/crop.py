import cv2
import os

files = os.listdir("Stock")

for file in files:
	img = cv2.imread("Stock/"+file)
	median = cv2.medianBlur(img,5)

