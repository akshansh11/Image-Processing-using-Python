# -*- coding: utf-8 -*-
"""
Created on Fri May 14 20:07:31 2021

@author: AKSHANSH MISHRA
"""

############ FEATURE DESCRIPTORS AND KEYPOINTS ###########

#Harris Corner Detector

import cv2
import numpy as np

img=cv2.imread("A:/brass.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)

harris=cv2.cornerHarris(gray,2,3,0.04)
img[harris>0.01*harris.max()]=[255,0,0]

cv2.imwrite("A:/Harris micro.png",img)


# Shi-Tomasi Corner Detector

import cv2
import numpy as np

img=cv2.imread("A:/brass.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners=cv2.goodFeaturesToTrack(gray,50,0.01,10)
corners=np.int0(corners)

for i in corners:
    x,y=i.ravel()
    cv2.circle(img,(x,y),3,255,-1)
cv2.imwrite("A:/Shi-Tomasi micro.png",img)    

#Harris and Shi-Tomasi are key point detectors. 

#FAST ALGORITHM FOR CORNER DETECTION

import cv2
import numpy as np

img=cv2.imread("A:/brass.jpg",0)

#Initiate FAST object with default values

detector=cv2.FastFeatureDetector_create(50)  #Detects 50 points
kp=detector.detect(img,None)
img2=cv2.drawKeypoints(img,kp,None,flags=0)
cv2.imwrite("A:/FAST micro.png",img2)

#ORIENTED FAST AND ROTATED BRIEF (ORB)
#FAST is a detector and BRIEF is a descriptor

import cv2
import numpy as np

img=cv2.imread("A:/brass.jpg",0)
orb=cv2.ORB_create(50)
kp,des=orb.detectAndCompute(img,None)

img2=cv2.drawKeypoints(img,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imwrite("A:/ORB micro2.png",img2)



                        