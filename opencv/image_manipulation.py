import cv2
import numpy as np 

#read image into matrix 
m = cv2.imread("download.png")

#get image properties 
h,w,bpp = np.shape(m)

#iterate over the entire image. 
for py in range(0,h):
	for px in range(0,w):
		m[py][px][0] = 0 

#display image 
#cv2.imshow('matrix',m)
#cv2.waitKey(0)

#save image 
cv2.imwrite('modified.png',m)
