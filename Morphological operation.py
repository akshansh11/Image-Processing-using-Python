# -*- coding: utf-8 -*-
"""
Created on Fri May 14 08:55:34 2021

@author: AKSHANSH MISHRA
"""

################ MORPHOLOGICAL OPERATIONS ##################

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("A:/tem.png",0)
plt.hist(img.flat,bins=100,range=(0,255))


#OTSU Based Thresholding

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("A:/tem.png",0)

ret,th=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite("F:/OTSU Thresholded tem.png",th)

#Erosion

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("A:/tem.png",0)

ret,th=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
kernel=np.ones((3,3),np.uint8)
print(kernel)
erosion=cv2.erode(th,kernel,iterations=1)

cv2.imwrite("F:/Eroded tem.png",erosion)

#Dilation

dilation=cv2.dilate(erosion,kernel,iterations=1)
cv2.imwrite("F:/Dilated tem.png",dilation)

#Opening

opening=cv2.morphologyEx(th,cv2.MORPH_OPEN,kernel)
cv2.imwrite("F:/Open Image tem.png",opening)

#Faster way to clean the image

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("A:/tem.png",0)
median=cv2.medianBlur(img,3)

ret,th=cv2.threshold(median,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite("F:/Thresholded new Image tem.png",th)
cv2.imwrite("F:/Median Image tem.png",median)



