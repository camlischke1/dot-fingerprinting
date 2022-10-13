from keras.utils import to_categorical
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#same results for same model, makes it deterministic
np.random.seed(1234)
tf.random.set_seed(1234)


#reading data
input = np.load("../Datasets/datasets_nav_whitepredict/coop_nav_whitebox_prediction_50.npy", allow_pickle=True)


pre = np.asarray(input[:,0])
a1 = np.asarray(input[:,1])
a2 = np.asarray(input[:,2])
a3 = np.asarray(input[:,3])
Y = np.asarray(input[:,5])

#flattens the np arrays
pre = np.concatenate(pre).ravel()
pre = np.reshape(pre, (pre.shape[0]//54,54))

X = np.column_stack((pre,a1.T,a2.T,a3.T))
X = X.astype('float64')


trainX = X[:180000]
trainY = Y[:180000]
valX = X[180000:]
valY = Y[180000:]
trainY = to_categorical(trainY)
valY = to_categorical(valY)


es = EarlyStopping(monitor='val_acc', mode='max', verbose=1, patience=100)
model = Sequential()
model.add(Dense(128, activation='relu'))
model.add(Dense(64,activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(valY.shape[1],activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
# fit network
history = model.fit(trainX, trainY, epochs=5000, batch_size=5000, verbose=2, validation_data = (valX,valY),shuffle=False,callbacks=es)

model.save('DenseNavWhitePredict.keras')