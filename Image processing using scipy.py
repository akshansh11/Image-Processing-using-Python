# -*- coding: utf-8 -*-
"""
Created on Sun May  9 09:54:55 2021

@author: AKSHANSH MISHRA
"""

#IMAGE PROCESSING USING SCIPY
 


from skimage import io
img=io.imread("A:/Data/SZ/sz1.png",as_gray=True)
print(type(img))
print(img.shape,img.dtype)
print(img)

print(img[10:15,20:25])

mean_grey=img.mean()
max_value=img.max()
min_value=img.min()
print("Mean, Max and Min value are:",mean_grey,max_value,min_value)

###############GEOMETRICAL TRANSFORMATIONS#######################

#Flipping the image

from skimage import io, img_as_ubyte
from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt
img=img_as_ubyte(io.imread("A:/Data/SZ/sz1.png",as_gray=True))
flippedLR=np.fliplr(img)
flippedUD=np.flipud(img)
plt.subplot(2,1,1)
plt.imshow(img,cmap="Greys")
plt.subplot(2,2,3)
plt.imshow(flippedLR,cmap="Blues")
plt.subplot(2,2,4)
plt.imshow(flippedUD,cmap="hsv")

#Rotating the image

from skimage import io, img_as_ubyte
from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt
img=img_as_ubyte(io.imread("A:/Data/SZ/sz1.png",as_gray=True))
rotated=ndimage.rotate(img,45, reshape=False)
plt.imshow(rotated)

############ IMAGE FILTERING ########################

#Uniform Filter is a type of blurring filter

from skimage import io, img_as_ubyte
from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt
img=img_as_ubyte(io.imread("A:/Data/SZ/sz1.png",as_gray=True))
uniform_filtered=ndimage.uniform_filter(img,size=9)
plt.imshow(uniform_filtered)

#Gaussian Filter is type of blurring filter which does not preserve the edges

from skimage import io, img_as_ubyte
from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt
img=img_as_ubyte(io.imread("A:/Data/SZ/sz1.png",as_gray=True))
gaussian_filtered=ndimage.gaussian_filter(img,sigma=7)
plt.imshow(gaussian_filtered)

#Median Filtering preserves the edges.

from skimage import io, img_as_ubyte
from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt
img=img_as_ubyte(io.imread("A:/Data/SZ/sz1.png",as_gray=True))
median_filtered=ndimage.uniform_filter(img,3)
plt.imshow(median_filtered)

sobel_img=ndimage.sobel(img,axis=0)
plt.imshow(sobel_img)
