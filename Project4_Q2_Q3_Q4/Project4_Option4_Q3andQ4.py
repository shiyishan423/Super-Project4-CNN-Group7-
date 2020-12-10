# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:34:12 2020

@author: Yishan Shi, Thadoe pyaethu, Wai Aung
"""

#Project4 Option4 Q3&Q4
import time
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import matplotlib.image as mpimg
start_time = time.time()

#loading the cifar10 dataset
from matplotlib import pyplot
from tensorflow.keras.datasets import cifar10
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

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
def run_example(name):
    # load the image
    path='./20samples/'
    img = load_image(path+name+'_32x32x3.png')
    # load model
    model = load_model('final_model.h5')
    # predict the class
    result = model.predict_classes(img)
    # print(result[0])
    return result[0]

#Print images.
def showPic(name):
    # entry point, run the example
    path='./20samples/'
    img = mpimg.imread(path+name+'_32x32x3.png')
    # imgplot = pyplot.imshow(img)
    # pyplot.show()
    return img

print('Predition Table:\n 0 = airplane \n 1 = automobile')
print(' 2 = bird\n 3 = cat \n 4 = deer \n 5 = dog\n 6 = frog')
print(' 7 = horse\n 8 = ship\n 9 = truck')
print('\n --------Loading the first 5 samples, Please Wait. Approximately: 30seconds --------\n')
cc = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']  

#Show 20 samples
w=10
h=10
fig=pyplot.figure(figsize=(15, 8))
columns = 5
rows = 1
label=[]
allnames=[]
for i in range(5):
    name=cc[i]+'1'
    img = showPic(name)
    a=run_example(name)
    label.append(a)
    allnames.append(cc[a])
    fig.add_subplot(rows, columns, i+1)
    pyplot.imshow(img)
pyplot.show()
print('Example training images and their labels: ', label) 
print('Corresponding classes for the labels: ' ,allnames)
print("Time used: %s seconds" % (time.time() - start_time))


print('\n --------Loading another 5 samples, Please Wait. Approximately: 30seconds--------\n')
w=10
h=10
fig=pyplot.figure(figsize=(15, 8))
columns = 5
rows = 1
label=[]
allnames=[]
for i in range(5):
    name=cc[i]+'2'
    img1 = showPic(name)
    a=run_example(name)
    label.append(a)
    allnames.append(cc[a])
    fig.add_subplot(rows, columns, i+1)
    pyplot.imshow(img1)
pyplot.show()
print('Example training images and their labels: ', label) 
print('Corresponding classes for the labels: ' ,allnames)
print("Time used: %s seconds" % (time.time() - start_time))

print('\n --------Loading another 5 samples, Please Wait. Approximately: 30seconds--------\n')
w=10
h=10
fig=pyplot.figure(figsize=(15, 8))
columns = 5
rows = 1
label=[]
allnames=[]
for i in range(5):
    x=i+5
    name=cc[x]+'1'
    img1 = showPic(name)
    a=run_example(name)
    label.append(a)
    allnames.append(cc[a])
    fig.add_subplot(rows, columns, i+1)
    pyplot.imshow(img1)
pyplot.show()
print('Example training images and their labels: ', label) 
print('Corresponding classes for the labels: ' ,allnames)
print("Time used: %s seconds" % (time.time() - start_time))

print('\n --------Loading the last 5 samples, Please Wait. Approximately: 30seconds--------\n')
w=10
h=10
fig=pyplot.figure(figsize=(15, 8))
columns = 5
rows = 1
label=[]
allnames=[]
for i in range(5):
    x=i+5
    name=cc[x]+'2'
    img1 = showPic(name)
    a=run_example(name)
    label.append(a)
    allnames.append(cc[a])
    fig.add_subplot(rows, columns, i+1)
    pyplot.imshow(img1)
pyplot.show()
print('Example training images and their labels: ', label) 
print('Corresponding classes for the labels: ' ,allnames)
print("Time used: %s seconds" % (time.time() - start_time))