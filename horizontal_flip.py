from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
import cv2
import random
import time
import os

rows = 150
cols = 150

origImage = 'archive/Ak/Ak (1).png'
outPath = 'augmented/'
# load the image
img = load_img(origImage)
# convert to numpy array
data = img_to_array(img)
# expand dimension to one sample
samples = expand_dims(data, 0)
# create image data augmentation generator
datagen = ImageDataGenerator(horizontal_flip=True)
# prepare iterator
it = datagen.flow(samples, batch_size=1)
# generate samples and plot
for i in range(0,9):
    pyplot.subplot(330 + 1 + i)
    batch = it.next()
    image = batch[0].astype('uint8')
    pyplot.imshow(image)
    imgPath = outPath + str(i) + ".png"
    image = cv2.resize(image, (rows, cols))
    cv2.imwrite(imgPath, image)
        
# show the figure
pyplot.show()