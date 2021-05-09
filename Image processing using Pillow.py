# -*- coding: utf-8 -*-
"""
Created on Sun May  9 06:51:17 2021

@author: AKSHANSH MISHRA
"""

#PILLOW LIBRARY FOR IMAGE PROCESSING

from PIL import Image
img=Image.open("A:/Data/HAZ/hz1.png")
print(img.size)

small_img=img.resize((200,150))
small_img.save("A:/Data/HAZ/hz1_small.png")

img.thumbnail((200,150))
img.save("A:/Data/HAZ/hz1_thumb.png")

#CROPPING
img=Image.open("A:/Data/HAZ/hz1.png")
cropped_image=img.crop((0,0,300,300))
cropped_image.save("A:/Data/HAZ/hz1_cropped.png")

#ROTATING THE IMAGE

img=Image.open("A:/Data/HAZ/hz1.png")
img90=img.rotate(45)
img90.save("A:/Data/HAZ/hz1_rotate.png")

#In order to keep the edges we can use 'expand' command

img=Image.open("A:/Data/HAZ/hz1.png")
img90=img.rotate(45, expand=True)
img90.save("A:/Data/HAZ/hz1_rotate45.png")

#FLIPPING THE IMAGE

#Left to Right Flipping


img=Image.open("A:/Data/HAZ/hz1.png")
image_flip=img.transpose(Image.FLIP_LEFT_RIGHT)     
image_flip.save("A:/Data/HAZ/hz1_LRflip.png")

#CHANGING THE IMAGE TO GREY SCALE
        
img=Image.open("A:/Data/HAZ/hz1.png")
grey_img=img.convert("L")
grey_img.save("A:/Data/HAZ/hz1_grey.png")

#AUTOMATE THE TASK ON NUMBER OF IMAGES

from PIL import Image
import glob
path="A:/Data/HAZ/*"
for file in glob.glob(path):
    print(file)
    a=Image.open(file)
    rotated90=a.rotate(90, expand=True)
    rotated90.save(file+"_rotated90.png")             