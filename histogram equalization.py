# -*- coding: utf-8 -*-
"""
Created on Thu May 13 11:35:25 2021

@author: AKSHANSH MISHRA
"""

########## HISTOGRAM EQUALIZATION #############

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("F:/two phase.png",0)
eq_img=cv2.equalizeHist(img)

plt.hist(img.flat,bins=100,range=(0,255))

plt.hist(eq_img.flat,bins=100,range=(0,255))

cv2.imwrite("F:/Equalized image.png",eq_img)


#Contrast Limited Adaptive Histogram Equalization

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("F:/two phase.png",0)
eq_img=cv2.equalizeHist(img)

clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
cl_img=clahe.apply(img)
cv2.imwrite("F:/CLAHE image.png",cl_img)

#Thresholding the image
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("F:/two phase.png",0)
eq_img=cv2.equalizeHist(img)

clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
cl_img=clahe.apply(img)
plt.hist(cl_img.flat,bins=100,range=(0,255))
ret,thres1=cv2.threshold(cl_img,190,150,cv2.THRESH_BINARY)
ret,thres2=cv2.threshold(cl_img,190,255,cv2.THRESH_BINARY_INV)
cv2.imwrite("F:/Binary Threshold 1.png",thres1)
cv2.imwrite("F:/Binary Threshold 2.png",thres2)

ret2,thres3=cv2.threshold(cl_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite("F:/OTSU.png",thres3)
