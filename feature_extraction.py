#from keras.utils import to_categorical
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import time
import threading

#this thread will sleep for a second and then kill the tshark process that hangs
def thread_function():
   time.sleep(.5)
   os.system("taskkill /f /im tshark.exe")

#reading data from source files
y = np.loadtxt("../CapstoneData/labels", dtype=int)
print(y.shape)

for i in range(0,2):#y.shape[0]):
   x = threading.Thread(target=thread_function)
   x.start()
   os.system("C:\\\"Program Files\"\Wireshark\\tshark.exe -r ../CapstoneData/dot.pcapng -Y (\"tcp.stream=={} and tls\") "
             "-T fields -E header=y -E separator=, -E occurrence=f -E quote=s -e tcp.stream -e ip.src -e ip.dst -e ip.len "
             "-e ip.ttl -e ip.proto -e tcp.window_size -e tcp.ack -e tcp.seq -e tcp.len -e frame.time_relative -e "
             "frame.time_delta -e tcp.time_relative -e tcp.time_delta -e tls.record.content_type -e _ws.col.Length -e "
             "tls.record.length -e tls.app_data ".format(i))

