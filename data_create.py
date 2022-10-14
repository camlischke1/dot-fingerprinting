#from keras.utils import to_categorical
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

#creating data
y = np.loadtxt("../CapstoneData/labels", dtype=int)
print(y.shape)


path = "../CapstoneData/dot.csv"        #assigning the csv file path
command = "C:\\Progra~1\Wireshark\\tshark.exe -r ../CapstoneData/dot.pcapng -Y tls "\
         "-T fields -E header=y -E separator=, -E occurrence=f -E quote=s -e tcp.stream -e ip.src -e ip.dst -e ip.len "\
         "-e ip.ttl -e ip.proto -e tcp.window_size -e tcp.ack -e tcp.seq -e tcp.len -e frame.time_relative -e "\
         "frame.time_delta -e tcp.time_relative -e tcp.time_delta -e tls.record.content_type -e _ws.col.Length -e "\
         "tls.record.length -e tls.app_data > {}".format(path)
os.system(command)

x = np.read_csv(path, ',', header=None)     #after creation of csv, read it into np array
np.save('dot.npy', x, allow_pickle=True)
print(x.shape)


