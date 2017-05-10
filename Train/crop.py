import cv2
import os

files = os.listdir("Temp")

for file in files:
	img = cv2.imread("Temp/"+file)
	img = img[:, 5:55]
	cv2.imwrite("Crop/"+file, img)
