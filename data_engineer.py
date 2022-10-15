#from keras.utils import to_categorical
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

x = np.load('../CapstoneData/dot.npy',allow_pickle=True)
print(x.shape)
y = np.load('../CapstoneData/y.npy',allow_pickle=True)
print(y.shape)
labels = np.load('../CapstoneData/labels.npy',allow_pickle=True)
print(labels.shape)