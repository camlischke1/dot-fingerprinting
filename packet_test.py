from keras.utils import to_categorical
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from tensorflow.python.keras.models import Sequential, load_model

# reading data
x = np.load("../CapstoneData/padded_x.npy", allow_pickle=True)
x = np.asarray(x).astype('float32')
y = np.load("../CapstoneData/padded_y.npy", allow_pickle=True)
#x = x[200000:]
#y = y[200000:]

# only use the 5th (index 4) packet in the stream (the query)
x = np.reshape(x[:,4,:],(x.shape[0],x.shape[2]))


model = load_model('PaddedPacketClassifier.keras')

pred = np.array(model.predict(x))
pred = np.argmax(pred,axis=1)

print(accuracy_score(y,pred))
print(classification_report(y,pred))
print(confusion_matrix(y,pred))

np.save("../CapstoneData/padded_yhat.npy",pred,allow_pickle=True)