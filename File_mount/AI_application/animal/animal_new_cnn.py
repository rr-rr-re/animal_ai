import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils

import keras

import tensorflow

classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50

#difine main func
def main():
