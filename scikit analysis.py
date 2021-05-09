# -*- coding: utf-8 -*-
"""
Created on Sun May  9 14:23:36 2021

@author: AKSHANSH MISHRA
"""

################ SCI-KIT IMAGE PROCESSING ############################

from skimage import io
from matplotlib import pyplot as plt
img=io.imread("A:/Data/SZ/sz1.png",as_gray=True)

from skimage.transform import rescale,resize,downscale_local_mean

rescaled_img=rescale(img,1.0/4.0,anti_aliasing=True)
resized_img=resize(img,(200,200),anti_aliasing=True)
downsized_img=downscale_local_mean(img,(4,9))
plt.imshow(rescaled_img)
plt.imshow(resized_img)
plt.imshow(downsized_img)


######################### EDGE DETECTION ###################################

from skimage import io
from matplotlib import pyplot as plt
img=io.imread("A:/brass.jpg",as_gray=True)

from skimage.filters import roberts, sobel, scharr, prewitt
edge_roberts=roberts(img)
plt.imshow(edge_roberts,cmap="gray")
edge_sobel=sobel(img)
edge_scharr=scharr(img)
edge_prewitt=prewitt(img)

plt.imshow(edge_sobel,cmap='gray')
plt.imshow(edge_scharr,cmap='gray')
plt.imshow(edge_prewitt,cmap='gray')

from skimage.feature import canny
edge_canny=canny(img,sigma=1)
plt.imshow(edge_canny)

####################### DECONVOLUTION ##########################

from skimage import io
from matplotlib import pyplot as plt
from skimage import restoration
img=io.imread("A:/Data/SZ/sz7.png",as_gray=True)
import numpy as np
psf=np.ones((3,3))/9
deconvolved,_=restoration.unsupervised_wiener(img,psf)

plt.imsave("A:/Data/SZ/deconvolved.png",deconvolved,cmap='gray')