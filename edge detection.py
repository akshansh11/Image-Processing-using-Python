# -*- coding: utf-8 -*-
"""
Created on Thu May 13 09:00:48 2021

@author: AKSHANSH MISHRA
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("A:/tem.png",1)

kernel=np.ones((3,3),np.float32)/9
filter_2D=cv2.filter2D(img,-1,kernel)
cv2.imshow("original",img)
cv2.imshow("Filter 2D",filter_2D)




#Blur Filter

blur=cv2.blur(img,(3,3))
cv2.imshow("Blurred Image",blur)

#Gaussian Blur

gaussian_blur=cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("Gaussian Filter",gaussian_blur)

#Median Filter

median_blur=cv2.medianBlur(img,3)
cv2.imshow("Median Filter",median_blur)

#Bilateral Blur



cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("F:/Filter 2D.png",filter_2D)
cv2.imwrite("F:/Blurred Image.png",blur)
cv2.imwrite("F:/Gaussian Filter.png",gaussian_blur)
cv2.imwrite("F:/Median Filter.png",median_blur)