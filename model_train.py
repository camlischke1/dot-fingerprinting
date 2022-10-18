from keras.utils import to_categorical
import numpy as np
from tensorflow.python.keras.callbacks import EarlyStopping
from tensorflow.python.keras.layers import LSTM, Dense
from tensorflow.python.keras.models import Sequential
import tensorflow as tf


#same results for same model, makes it deterministic
#np.random.seed(1234)
tf.random.set_seed(1234)


#reading data
x = np.load("../CapstoneData/x.npy", allow_pickle=True)
x = np.asarray(x).astype('float32')
y = np.load("../CapstoneData/y.npy", allow_pickle=True)
print(np.unique(y))
y = to_categorical(y)
print(y.shape)

'''
trainX = x[:150000]
trainY = y[:150000]
valX = x[150000:170000]
valY = y[150000:170000]


es = EarlyStopping(monitor='val_acc', mode='max', verbose=1, patience=100)
model = Sequential()
model.add(LSTM(64,return_sequences=True,input_shape=(trainX.shape[1],trainX.shape[2])))
model.add(LSTM(32))
model.add(Dense(16, activation='relu'))
#number nodes in this layer corresponds to agent's possible decisions:it can go to 0,1,or 2 (MULTI-CLASS CLASSIFICATION)
model.add(Dense(valY.shape[1],activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
# fit network
history = model.fit(trainX, trainY, epochs=5000, batch_size=5000, verbose=2, validation_data = (valX,valY),shuffle=False,callbacks=es)

model.save('UnpaddedLSTM.keras')
'''