# -*- coding: utf-8 -*-
"""
Created on Mon May 10 17:33:19 2021

@author: AKSHANSH MISHRA
"""

############## DENOISING FILTERS ###################

#Digital Filters are just convolution between the kernel and the given image.
#Convolution is just the multiplication of two arrays of different sizes.
#Kernel can be a linear filter such as a Gaussian Filter and other can be non-linear such as Median filter.
#Non-Linear filter preserves the edges.

##### Gaussian Filter #####

from skimage import io
from scipy import ndimage as nd
from matplotlib import pyplot as plt

img=io.imread("A:/Data/SZ/sz1.png")
gaussian_image=nd.gaussian_filter(img,sigma=3)
plt.imsave("A:/Data/SZ/gaussian.png",gaussian_image)

#The obtained image is completely blurred and the there is information loss from the image.

###### Median Filter ######

median_image=nd.median_filter(img,size=3)
plt.imsave("A:/Data/SZ/median.png",median_image)

#It is observed that the obtained image form median filter is much better than the gaussian filter and the information is preserved.

median_image=nd.median_filter(img,size=5)
plt.imsave("A:/Data/SZ/median2.png",median_image)

#At kernel size of 5 there is an information loss at edges from the image.

############### Non-Local Means Filter ####################

from skimage.restoration import denoise_nl_means,estimate_sigma
from skimage import img_as_float
import numpy as np
img=img_as_float(io.imread("A:/Data/SZ/sz1.png"))
sigma_est=np.mean(estimate_sigma(img,multichannel=True))

non_local_means=denoise_nl_means(img,h=1.15*sigma_est,fast_mode=True,patch_size=5,patch_distance=3,multichannel=True)
plt.imsave("A:/Data/SZ/nonlocal.png",non_local_means)

#It is observed that the edges are perfectly preserved and noise is removed. 

