from keras.utils import to_categorical
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from tensorflow.python.keras.models import Sequential, load_model

# reading data
x = np.load("../CapstoneData/x.npy", allow_pickle=True)
x = np.asarray(x).astype('float32')
y = np.load("../CapstoneData/y.npy", allow_pickle=True)

# only use the 5th (index 4) packet in the stream (the query)
x = np.reshape(x[:,5,:],(x.shape[0],x.shape[2]))

testX = x[170000:]
testY = y[170000:]
print(np.unique(testY,return_counts=True))

model = load_model('UnpaddedDense.keras')

pred = np.array(model.predict(testX))
pred = np.argmax(pred,axis=1)

print(accuracy_score(testY,pred))
print(classification_report(testY,pred))
print(confusion_matrix(testY,pred))