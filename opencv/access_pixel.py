import cv2
import numpy as np 

#read image into matrix 
m = cv2.imread("download.png")

# get image properties 
h,w,bpp = np.shape(m)

#print pixel value
y = 1 
x = 1
print m[y][x]

#interate over the entire image. 
for py in range(0,h):
	for px in range(0,w):
		print m[py][px]		

