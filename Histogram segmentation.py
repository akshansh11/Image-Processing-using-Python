# -*- coding: utf-8 -*-
"""
Created on Tue May 11 21:42:00 2021

@author: AKSHANSH MISHRA
"""

########### HISTOGRAM SEGMENTATION #################

from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import img_as_float, img_as_ubyte,io
import numpy as np
from matplotlib import pyplot as plt

img=img_as_float(io.imread("A:/brass.jpg"))

sigma_est=np.mean(estimate_sigma(img,multichannel=True))
denoise=denoise_nl_means(img,h=1.15*sigma_est,fast_mode=True,patch_size=5,patch_distance=3,multichannel=True)
denoise_ubyte=img_as_ubyte(denoise)
plt.imshow(denoise_ubyte,cmap='gray')

plt.hist(denoise_ubyte.flat,bins=100,range=(0,255))

seg1=(denoise_ubyte<=55)
seg2=(denoise_ubyte>55)&(denoise_ubyte<=110)
seg3=(denoise_ubyte>110)&(denoise_ubyte<=210)
seg4=(denoise_ubyte>210)

all_segments=np.zeros((denoise_ubyte.shape[0],denoise_ubyte.shape[1],3))

all_segments[seg1]=(1,0,0)
all_segments[seg2]=(0,1,0)
all_segments[seg3]=(0,0,1)
all_segments[seg4]=(1,1,0)
plt.imshow(all_segments)
