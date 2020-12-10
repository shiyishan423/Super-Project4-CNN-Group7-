# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:49:28 2020

@author: Yishan Shi, Thadoe pyaethu, Wai Aung
"""
#Project4 - Option4 - Q2
from PIL import Image
import matplotlib.image as mpimg
from matplotlib import pyplot

#digitize the image to 32x32x3 pixel format.
img = Image.open('airplane1.jpg') # image extension *.png,*.jpg
print('Original Image:')
imgplot = pyplot.imshow(img)
pyplot.show()
new_width  = 32
new_height = 32
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('airplane1_32x32x3.png') # format may what you want *.png, *jpg, *.gif
imgplot = pyplot.imshow(img)
print('\nImage with 32x32x3 pixel format:')
pyplot.show()

#Convert and save 20 image samples to 32x32x3 pixel format.
def newFormat(name):
    path='./20samples/'
    img = Image.open(path+name+ '.jpg') # image extension *.png,*.jpg
    print('\nOriginal Image:')
    imgplot = pyplot.imshow(img)
    pyplot.show()
    new_width  = 32
    new_height = 32
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img.save(path+name+'_32x32x3.png') # format may what you want *.png, *jpg, *.gif
    imgplot = pyplot.imshow(img)
    print('\nImage with 32x32x3 pixel format:')
    pyplot.show()

#Convert and print all 20 new images.
#The 20 Images with the new format are saved under the same file.
newFormat('airplane1')
newFormat('airplane2')
newFormat('bird1')
newFormat('bird2')
newFormat('automobile1')
newFormat('automobile2')
newFormat('cat1')
newFormat('cat2')
newFormat('deer1')
newFormat('deer2')
newFormat('dog1')
newFormat('dog2')
newFormat('frog1')
newFormat('frog2')
newFormat('horse1')
newFormat('horse2')
newFormat('ship1')
newFormat('ship2')
newFormat('truck1')
newFormat('truck2')

