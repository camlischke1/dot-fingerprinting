#from keras.utils import to_categorical
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

#creating data
y = np.loadtxt("../CapstoneData/labels", dtype=int)
print(y.shape)


path = "../CapstoneData/dot.csv"        #assigning the csv file path
'''
command = "C:\\Progra~1\Wireshark\\tshark.exe -r ../CapstoneData/dot.pcapng -Y tls "\
         "-T fields -E header=y -E separator=, -E occurrence=f -E quote=n -e tcp.stream -e ip.src -e ip.dst -e ip.len "\
         "-e ip.ttl -e ip.proto -e tcp.window_size -e tcp.ack -e tcp.seq -e tcp.len -e frame.time_relative -e "\
         "frame.time_delta -e tcp.time_relative -e tcp.time_delta -e tls.record.content_type -e _ws.col.Length -e "\
         "tls.record.length -e tls.app_data > {}".format(path)
os.system(command)
'''
df = pd.read_csv(path)     #after creation of csv, read it into dataframe
headers = list(df.columns)
print(headers)

#reshape dataframe
x = []
stream_list = []
for i in range(0,df.shape[0]-1):
    stream_id = int(df.iloc[i]['tcp.stream'])            #gets the stream id
    stream_id2 = int(df.iloc[i+1]['tcp.stream'])
    stream_list.append(df.iloc[i][headers[1:]].values)

    if (stream_id != stream_id2):           #if the next packet is not in this stream, recreate stream_list
        x.append(stream_list)
        stream_list = []

x = np.asarray(x)
print(x.shape)
np.save('dot.npy', x, allow_pickle=True)
