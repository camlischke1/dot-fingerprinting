#from keras.utils import to_categorical
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

path = "../CapstoneData/dot.csv"        #assigning the csv file path


#creating data
labels = pd.read_csv("../CapstoneData/labels.txt", header=None)
print(labels.shape)
y = np.asarray(labels[0].tolist())
labels = np.asarray(labels[1].tolist())
np.save('../CapstoneData/y.npy', y, allow_pickle=True)
np.save('../CapstoneData/urls.npy', y, allow_pickle=True)

print("Writing .csv file...")
command = "C:\\Progra~1\Wireshark\\tshark.exe -r ../CapstoneData/dot.pcapng -Y tls "\
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
for i in range(0,df.shape[0]-1):
    stream_id = int(df.iloc[i]['tcp.stream'])            #gets the stream id
    stream_id2 = int(df.iloc[i+1]['tcp.stream'])
    stream_list.append(df.iloc[i][headers[1:]].values)

    if (stream_id != stream_id2):           #if the next packet is not in this stream, recreate stream_list
        x.append(stream_list)
        stream_list = []
    if i%100000 == 0:                       #print for progress
        print(i)

# get the last 7 packets too
stream_list.append(df.iloc[df.shape[0]-1][headers[1:]].values)
x.append(stream_list)


print("Saving...")
x = np.asarray(x)
print(x.shape)
np.save('../CapstoneData/dot_raw.npy', x, allow_pickle=True)