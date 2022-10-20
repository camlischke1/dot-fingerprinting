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
x = np.load("../CapstoneData/padded_x.npy", allow_pickle=True)
x = np.asarray(x).astype('float32')
y = np.load("../CapstoneData/padded_y.npy", allow_pickle=True)
print(np.unique(y,return_counts=True))
y = to_categorical(y)

#only use the 5th (index 4) packet in the stream (the query)
x = np.reshape(x[:,4,:],(x.shape[0],x.shape[2]))

trainX = x[:180000]
trainY = y[:180000]
valX = x[180000:200000]
valY = y[180000:200000]


es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=100)
model = Sequential()
model.add(Dense(128, activation='relu'))
model.add(Dense(64,activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(valY.shape[1],activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
# fit network
history = model.fit(trainX, trainY, epochs=5000, batch_size=5000, verbose=2, validation_data = (valX,valY),shuffle=False,callbacks=es)

model.save('PaddedPacketClassifier.keras')
np.save("../CapstoneData/padded_history.npy", history.history, allow_pickle=True)
