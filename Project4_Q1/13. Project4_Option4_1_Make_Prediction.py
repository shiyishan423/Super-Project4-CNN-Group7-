# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:21:47 2020

@author: Yishan Shi, Thadoe pyaethu, Wai Aung
"""

# make a prediction for a new image.
import time
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import matplotlib.image as mpimg
from matplotlib import pyplot
start_time = time.time()


# load and prepare the image
def load_image(filename):
    # load the image
    img = load_img(filename, target_size=(32, 32))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(1, 32, 32, 3)
    # prepare pixel data
    img = img.astype('float32')
    img = img / 255.0
    return img

# load an image and predict the class
def run_example():
    # load the image
    img = load_image('sample_image.png')
    # load model
    model = load_model('final_model.h5')
    # predict the class
    result = model.predict_classes(img)
    print(result[0])


# entry point, run the example
run_example()
print("Time used: %s seconds" % (time.time() - start_time))

img = mpimg.imread('sample_image.png')
imgplot = pyplot.imshow(img)
pyplot.show()