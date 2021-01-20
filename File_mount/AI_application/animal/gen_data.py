from PIL import Image
import os, glob
import numpy as np
from sklearn import cross_validation

classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50

# 画像の読み込み
X = []
Y = []
