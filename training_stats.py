import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import load_model

unpadded_binary = np.load("../CapstoneData/history.npy", allow_pickle=True).item()
padded_binary = np.load("../CapstoneData/padded_history.npy", allow_pickle=True).item()
padded_multi = np.load("../CapstoneData/multi_padded_history.npy", allow_pickle=True).item()
unpadded_multi = np.load("../CapstoneData/multi_history.npy", allow_pickle=True).item()

model = load_model("PaddedClassifier.keras")
model.summary()


plt.plot(unpadded_binary['val_acc'], label='Binary')
plt.plot(unpadded_multi['val_acc'], label='Multi')
plt.title("Validation Accuracy per Training Episode for Unpadded DoT")
plt.legend()
plt.show()


plt.plot(padded_binary['val_acc'], label='Binary')
plt.plot(padded_multi['val_acc'], label='Multi')
plt.title("Validation Accuracy per Training Episode for Padded DoT")
plt.legend()
plt.show()