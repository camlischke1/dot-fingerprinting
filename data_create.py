#from keras.utils import to_categorical
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tqdm import tqdm
import os

path = "../CapstoneData/multi_padded_dot.csv"        #assigning the csv file path


#creating data
labels = pd.read_csv("../CapstoneData/multi_labels.txt", header=None)
print(labels.shape)
y = np.asarray(labels[0].tolist())
labels = np.asarray(labels[1].tolist())

print("Writing .csv file...")
command = "C:\\Progra~1\Wireshark\\tshark.exe -r ../CapstoneData/multi_padded_dot.pcapng -Y tls "\
         "-T fields -E header=y -E separator=, -E occurrence=f -E quote=n -e tcp.stream -e ip.dst -e ip.len "\
         "-e tcp.window_size -e tcp.ack -e tcp.seq -e tcp.len -e frame.time_relative -e "\
         "frame.time_delta -e tcp.time_relative -e tcp.time_delta -e tls.record.content_type -e _ws.col.Length -e "\
         "tls.record.length -e tls.app_data -e frame.len > {}".format(path)
os.system(command)

df = pd.read_csv(path)     #after creation of csv, read it into dataframe
headers = list(df.columns)
print(headers)

print("Shaping dataframe by tcp stream id...")
x = []
stream_list = []
for i in tqdm(range(df.shape[0]-1)):
    stream_id = int(df.iloc[i]['tcp.stream'])            #gets the stream id
    stream_id2 = int(df.iloc[i+1]['tcp.stream'])
    stream_list.append(df.iloc[i][headers[1:]].values)

    if (stream_id != stream_id2):           # if the next packet is not in this stream, recreate stream_list
        if len(stream_list) == 7:           # make sure it has 7 packets, don't include in dataset otherwise
            x.append(stream_list)
        else:
            y = np.delete(y,stream_id,0)
            labels = np.delete(labels, stream_id, 0)
        stream_list = []

# get the last 7 packets too
stream_list.append(df.iloc[df.shape[-1]][headers[1:]].values)
x.append(stream_list)


print("Saving...")
x = np.asarray(x)
print(x.shape)
np.save('../CapstoneData/multi_padded_dot_raw.npy', x, allow_pickle=True)
np.save('../CapstoneData/multi_padded_y.npy', y, allow_pickle=True)
np.save('../CapstoneData/multi_padded_labels.npy', labels, allow_pickle=True)