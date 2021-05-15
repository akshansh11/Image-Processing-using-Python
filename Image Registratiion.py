# -*- coding: utf-8 -*-
"""
Created on Sat May 15 08:02:48 2021

@author: AKSHANSH MISHRA
"""

##################### IMAGE REGISTRATION ###########################

#ORB

import cv2
import numpy as np

img=cv2.imread("A:/Data/HAZ/hz1.png")
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Initiate ORB

orb=cv2.ORB_create(50)
kp,des=orb.detectAndCompute(img1,None)
img2=cv2.drawKeypoints(img1,kp,None,flags=None)

cv2.imwrite("A:/hz1 orb.png",img2)



#Task to be completed
# 1. Import two microstructure images
# 2. Convert to grayscale
# 3. Initiate ORB Detector
# 4. Find key points and describe them
# 5. Match the keypoints between two images by using Brute Force Matcher
# 6. Rejecting the bad keypoints by using RANSAC
# 7. Register the images using Homology

import cv2
import numpy as np

im2=cv2.imread("A:/Data/HAZ/hz1.png") #Reference Image
im1=cv2.imread("A:/Data/HAZ/hz1_rotate.png")  #Image to be registered

img1=cv2.cvtColor(im1,cv2.COLOR_BGR2GRAY)
img2=cv2.cvtColor(im2,cv2.COLOR_BGR2GRAY)

#Initiate ORB

orb=cv2.ORB_create(50)
kp1,des1=orb.detectAndCompute(img1,None)
kp2,des2=orb.detectAndCompute(img2,None)

matcher=cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)

#Match Desriptor
matches=matcher.match(des1,des2,None)

matches=sorted(matches,key=lambda x:x.distance)

img5=cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None)
points1=np.zeros((len(matches),2),dtype=np.float32)
points2=np.zeros((len(matches),2),dtype=np.float32)
for i,match in enumerate(matches):
    points1[i,:]=kp1[match.queryIdx].pt
    points2[i,:]=kp2[match.trainIdx].pt
h,mask=cv2.findHomography(points1,points2,cv2.RANSAC)

#Use Homography
height,width,channels=im2.shape
im1Reg=cv2.warpPerspective(im1,h,(width,height))
img5=cv2.drawMatches(im1,kp1,im2,kp2,matches[:10],None)

cv2.imwrite("A:/Registered micros.png",im1Reg)
cv2.imwrite("A:/Keypoint matches.png",img5)

    
cv2.imwrite("A:/Matches.png",img5)
img3=cv2.drawKeypoints(img2,kp1,None,flags=None)
img4=cv2.drawKeypoints(img1,kp2,None,flags=None)

cv2.imwrite("A:/hz1 reference.png",img3)
cv2.imwrite("A:/hz1 to referenced.png",img4)




