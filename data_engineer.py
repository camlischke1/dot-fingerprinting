# from keras.utils import to_categorical
import numpy as np
import hashlib
import math
from sklearn import preprocessing
from tqdm import tqdm

print("Loading...")
x = np.load('../CapstoneData/multi_padded_dot_raw.npy', allow_pickle=True)
print(x.shape)

# The headers below relate to the attributes in each of the captured packets, after the above modifications

# 0-ip.dest    1-ip.len   2-tcp.window_size   3-tcp.ack   4-tcp.seq
# 5-tcp.len   6-frame.time_relative   7-frame.time_delta     8-tcp.time_relative    9-tcp.time_delta
# 10-tls.record.content_type  11-_ws.col.Length   12-tls.record.length    13-tls.app_data   14-frame.len

print("Hashing encrypted data and removing NaN...")
# convert tls.app_data (encrypted data string) to hash of 8 bytes and then convert hash to integer
for i in tqdm(range(x.shape[0])):
    x[i, 4, 13] = int("0x" + x[i, 4, 13][16:32],16)
    x[i, 5, 13] = int("0x" + x[i, 5, 13][16:32],16)
    for j in range(x.shape[1]):
        for k in range(1,x.shape[2]):
            if (isinstance(x[i, j, k], float)):
                if math.isnan(x[i, j, k]):
                    x[i, j, k] = 0

print("Extracting features...")
# make sourceIP into binary value of sent by client 64bytes(-1), sent by server 128bytes(1)
x[:,:,0] = np.where(x[:,:,0] == '192.168.126.122',1,-1)    # destination is client IP
# make make tls.record.content_type map to 0,1,2,3 respectively
x[:,:,10] = np.subtract(x[:,:,10],20)
x[:,:,10] = x[:,:,10].astype(int)

print("Normalizing...")
#convert to float to make normalization easy
x = np.array(x,dtype='float64')
for i in tqdm(range(x.shape[2])):
    mean = np.mean(x[:,:,i])
    std = np.std(x[:,:,i])
    x[:, :, i] = x[:, :, i] - mean
    x[:, :, i] = x[:, :, i] / std


print("Saving...")
np.save('../CapstoneData/multi_padded_x_int.npy',x)
