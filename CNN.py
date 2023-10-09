#pip install --upgrade tensorflow==2.0.0-rc1
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
from os import path
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
import tensorflow.keras.backend as K
from tensorflow.keras.applications import VGG16
from tensorflow.keras.preprocessing.image import ImageDataGenerator

model_name = 'vgg16.model'

rows = 150
cols = 150
channels = 3
train_dir = 'augmented/'

if(path.exists(model_name)) :
    model = keras.models.load_model(model_name)
else :
    test_dir = train_dir
    validation_dir = train_dir
    classes = 5
    
    train_datagen = ImageDataGenerator(rescale=1.0/255)
    test_datagen = ImageDataGenerator(rescale=1.0/255)
    validation_datagen = ImageDataGenerator(rescale=1.0/255)
    
    train_batch_size = 32 #Use 32 images to train in one steps
    np.random.seed(100)
    
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(rows,cols),
        batch_size=train_batch_size,
        class_mode='categorical')
    
    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(rows,cols),
        batch_size=train_batch_size,
        class_mode='categorical')
    
    validation_generator = validation_datagen.flow_from_directory(
        validation_dir,
        target_size=(rows,cols),
        batch_size=train_batch_size,
        class_mode='categorical')
    
    conv_base = VGG16(weights='imagenet',
                  include_top=False,
                  input_shape=(rows,cols,channels))
    
    conv_base.trainable = False;
    model = models.Sequential()
    model.add(conv_base)
    
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(256,activation='relu'))
    model.add(keras.layers.Dense(classes,activation='softmax'))
    
    print(model.summary())
    
    model.compile(loss='categorical_crossentropy',
                  optimizer='sgd',
                  metrics=['accuracy'])
    checkpoint_callback = keras.callbacks.ModelCheckpoint(model_name,
                                                             save_best_only=True)
    model_history = model.fit_generator(
        train_generator,
        steps_per_epoch=20,
        epochs = 10,
        validation_data=validation_generator,
        validation_steps=50,
        callbacks = [checkpoint_callback])
    
    model.save(model_name)