# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 11:09:57 2017
"""
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model
from keras.preprocessing import image as kim
import os
import numpy as np
import scipy.misc as mi

def noiseItUp(image):
    scale = np.random.rand()*80 + 20
    shape = image.shape
    n = (np.random.rand(*shape)-0.5) * scale
    print(np.max(n),np.min(n))
    return image + n


def getModel():
    inp = Input(shape=(299,299,3))
    x = Conv2D(16, (3,3), activation='relu', padding='same')(inp)
    x = Conv2D(32, (3,3), activation='relu', padding='same')(x)
    x = MaxPooling2D((2,2),padding='same')(x)
    x = Conv2D(32, (3,3), activation='relu', padding='same')(x)
    encoded = MaxPooling2D((2,2),padding='same')(x)

    x = Conv2D(8, (3, 3), activation='relu', padding='same')(encoded)
    x = UpSampling2D((2, 2))(x)
    x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
    x = UpSampling2D((2, 2))(x)
    x = Conv2D(16, (3, 3), activation='relu')(x)
    x = UpSampling2D((2, 2))(x)
    decoded = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(x)
    return Model(inp, decoded)


ACTUAL_SIZE = (299,299)
READ_IN_SIZE = (304,304)

gen = kim.ImageDataGenerator(rotation_range=8, width_shift_range=0.02,
                              height_shift_range=0.02, shear_range=0.,
                              preprocessing_function=noiseItUp)
#its = gen.flow_from_directory("data/images_in/", target_size=(299,299),
#                              save_to_dir="data/images_out/")

# define our model
model = getModel()

# iterate over the input image folder, creating examples
imPath = "data/images_in/dog/"
ls = os.listdir(imPath)

out = []
inps = []
for fn in ls:
    img = kim.load_img(imPath+fn, target_size=READ_IN_SIZE)
    img = img.resize(ACTUAL_SIZE)
    x = kim.img_to_array(img)
    outputImg = x.copy()
    outs[n] = 
    x = noiseItUp(x)
    x = gen.random_transform(x)
    
    img = kim.array_to_img(x)
    mi.imsave("data/images_out/example_"+fn,img)
