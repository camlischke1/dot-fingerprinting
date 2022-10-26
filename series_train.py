from keras.utils import to_categorical
import numpy as np
from tensorflow.python.keras.callbacks import EarlyStopping
from tensorflow.python.keras.layers import LSTM, Dense
from tensorflow.python.keras.models import Sequential
import tensorflow as tf

tf.random.set_seed(1234)

#reading data
x = np.load("../CapstoneData/multi_padded_x_int.npy", allow_pickle=True)
x = np.asarray(x).astype('float32')
y = np.load("../CapstoneData/multi_padded_y.npy", allow_pickle=True)
print(np.unique(y,return_counts=True))
y = to_categorical(y)

#only use the 5th (index 4) packet in the stream (the query)
x = np.reshape(x[:,4:6,:],(x.shape[0],2,x.shape[2]))
print(x.shape)
print(x[0])

trainX = x[:180000]
trainY = y[:180000]
valX = x[180000:200000]
valY = y[180000:200000]

es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=100)
model = Sequential()
model.add(LSTM(64,return_sequences=True,input_shape=(trainX.shape[1],trainX.shape[2])))
model.add(LSTM(32))
model.add(Dense(16, activation='relu'))
#number nodes in this layer corresponds to agent's possible decisions:it can go to 0,1,or 2 (MULTI-CLASS CLASSIFICATION)
model.add(Dense(valY.shape[1],activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])
# fit network
history = model.fit(trainX, trainY, epochs=5000, batch_size=5000, verbose=2, validation_data = (valX,valY),shuffle=False,callbacks=es)

model.save('PaddedMultiLSTM.keras')