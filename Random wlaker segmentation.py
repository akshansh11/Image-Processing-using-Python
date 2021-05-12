# -*- coding: utf-8 -*-
"""
Created on Wed May 12 12:15:49 2021

@author: AKSHANSH MISHRA
"""

######### RANDOM WALKER SEGMENTATION ###########

from skimage import io,img_as_float
import matplotlib.pyplot as plt
from skimage.restoration import denoise_nl_means, estimate_sigma
import numpy as np

img=img_as_float(io.imread("A:/tem.png"))

plt.hist(img.flat,bins=100,range=(0,1))

#We can denoise the imag to get good histogram 

sigma_est=np.mean(estimate_sigma(img,multichannel=True))
patch_kw=dict(patch_size=5,patch_distance=6,multichannel=True)
denoise_img=denoise_nl_means(img,h=1.15*sigma_est,fast_mode=True,**patch_kw)
plt.hist(denoise_img.flat,bins=100,range=(0,1))


from skimage import exposure 
eq_img=exposure.equalize_adapthist(denoise_img)
plt.hist(eq_img.flat,bins=100,range=(0,1))

#It is observed that the histogram has been stretched. 

plt.imshow(eq_img,cmap='gray')

markers=np.zeros(img.shape,dtype=np.uint)
markers[(eq_img<0.6)&(eq_img>0.3)]=1
markers[(eq_img>0.8)&(eq_img<0.99)]=2
plt.imshow(markers)

from skimage.segmentation import random_walker
labels=random_walker(eq_img,markers,beta=10,mode='bf')
plt.imshow(labels)