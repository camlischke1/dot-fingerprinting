from keras.utils import to_categorical
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from tensorflow.python.keras.models import Sequential, load_model

def plot_confusion_matrix(cm,
                          target_names,
                          title='Confusion matrix',
                          cmap=None,
                          normalize=True):

    import matplotlib.pyplot as plt
    import numpy as np
    import itertools

    accuracy = np.trace(cm) / np.sum(cm).astype('float')
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=45)
        plt.yticks(tick_marks, target_names)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]


    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")


    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass))
    plt.show()




# reading data
x = np.load("../CapstoneData/padded_x.npy", allow_pickle=True)
x = np.asarray(x).astype('float32')
y = np.load("../CapstoneData/padded_y.npy", allow_pickle=True)
x = x[200000:]
y = y[200000:]

# only use the 5th (index 4) packet in the stream (the query)
x = np.reshape(x[:,4,:],(x.shape[0],x.shape[2]))


model = load_model('PaddedClassifier.keras')

pred = np.array(model.predict(x))
pred = np.argmax(pred,axis=1)

print(accuracy_score(y,pred))
print(classification_report(y,pred))
print(confusion_matrix(y,pred))

np.save("../CapstoneData/padded_yhat.npy",pred,allow_pickle=True)
values, counts = np.unique(y, return_counts=True)

if (len(counts)==2):
    target_names = ["ubuntu-dns","not ubuntu-dns"]
    plot_confusion_matrix(confusion_matrix(y,pred),target_names,title='',normalize=False)

if (len(counts)==7):
    target_names = ["ubuntu-dns","a","cam","howlongcan...","windows-dns","windows-client","ubuntu-client"]
    plot_confusion_matrix(confusion_matrix(y,pred),target_names,title='',normalize=False)