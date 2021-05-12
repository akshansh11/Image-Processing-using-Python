# -*- coding: utf-8 -*-
"""
Created on Thu May 13 00:29:51 2021

@author: AKSHANSH MISHRA
"""

import cv2
img=cv2.imread("A:/brass.jpg",1)
print(img.shape)

#To look the pixel values

print("Top Left",img[0,0])

#In opencv the convention of image reading is BGR

print("Top Right",img[0,200])
print("Bottom Left",img[160,0])
print("Bottom Right",img[160,200])


########### SPLITTING THE CHANNELS ###############

import cv2
img=cv2.imread("A:/brass.jpg",1)
blue=img[:,:,0]
green=img[:,:,1]
red=img[:,:,2]
cv2.imshow("Blue Pixels",blue)
cv2.imshow("Green Pixels",green)
cv2.imshow("Red Pixels",red)
cv2.waitKey(0)
cv2.DestroyAllWindows()

#Splitting shortcut

import cv2
img=cv2.imread("A:/brass.jpg",1)

blue,gree,red=cv2.split(img)

cv2.imshow("Blue Pixels",blue)
cv2.imshow("Green Pixels",green)
cv2.imshow("Red Pixels",red)
cv2.waitKey(0)
cv2.DestroyAllWindows()