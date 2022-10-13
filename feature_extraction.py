#from keras.utils import to_categorical
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import time
import threading

#this thread will sleep for a second and then kill the tshark process that hangs
def thread_function():
   time.sleep(1)
   os.system("taskkill /f /im tshark.exe")

#reading data from source files
y = np.loadtxt("../CapstoneData/labels", dtype=int)
print(y.shape)

for i in range(0,2):#y.shape[0]):
   x = threading.Thread(target=thread_function)
   x.start()
   os.system("del dot.csv")
   os.system("touch dot.csv")
   os.system("C:\\\"Program Files\"\Wireshark\\tshark.exe -r ../CapstoneData/dot.pcapng -Y (\"tcp.stream=={} and tls\") -T fields -E header=y -E separator=, -E occurrence=f -E quote=s -e tcp.stream -e ip.src -e ip.dst -e ip.len -e ip.ttl -e ip.proto -e tcp.window_size -e tcp.ack -e tcp.seq -e tcp.len -e frame.time_relative -e frame.time_delta -e tcp.time_relative -e tcp.time_delta -e tls.record.content_type -e _ws.col.Length -e tls.record.length -e tls.app_data ".format(i))


'''
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
'''