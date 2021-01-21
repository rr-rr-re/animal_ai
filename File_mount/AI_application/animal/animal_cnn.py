from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
import numpy as np

classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50

#difine main func
def maim():
    X_train, X_test, Y_train, Y_test = np.load("./animal.npy")
    X_train = X_train.astype("float") / 256
    X_test = X_test.astype("float") / 256
    Y_train = np.utils.to_categorical(Y_train, num_classes)
    Y_test = np.utils.to_categorical(Y_test, num_classes)

    model = model_train(X_train, Y_train)
    model_eval(model, X_test, Y_test)

def model_train():
    model =
