#!/usr/bin/env python
import cv2
import numpy as np

#read image into matrix 
m = cv2.imread("download.png")

#get image properties. 
h,w,bpp = np.shape(m)

#print image properties 
print "width: " + str(w)
print "height: " + str(h)
print "bpp: " + str(bpp)
