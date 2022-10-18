# from keras.utils import to_categorical
import numpy as np
import hashlib
import math
from sklearn import preprocessing

print("Loading...")
x = np.load('../CapstoneData/dot.npy', allow_pickle=True)

print("Deleting redundant data...")
# delete redundant data attributes
x = np.delete(x, 0, 2)      # source IP (covered by dest IP)
x = np.delete(x, 3, 2)      # ip.protocol is '6' for all packets
x = np.delete(x, 2, 2)      # IP ttl covered by source IP


# The headers below relate to the attributes in each of the captured packets.

# 0-ip.dest    1-ip.len   2-tcp.window_size   3-tcp.ack   4-tcp.seq
# 5-tcp.len   6-frame.time_relative   7-frame.time_delta     8-tcp.time_relative    9-tcp.time_delta
# 10-tls.record.content_type  11-_ws.col.Length   12-tls.record.length    13-tls.app_data

print("Extracting features...")
# make sourceIP into binary value of sent by client 64bytes(-1), sent by server 128bytes(1)
x[:,:,0] = np.where(x[:,:,0] == '192.168.126.122',1,-1)    # destination is client IP

# make make tls.record.content_type map to 0,1,2,3 respectively
x[:,:,9] = np.subtract(x[:,:,9],20)
x[:,:,9] = x[:,:,9].astype(int)

print("Hashing encrypted data...")
# convert tls.app_data (encrypted data string) to hash of 8 bytes and then convert hash to integer
for i in range(x.shape[0]):
    x[i, 4, 13] = int("0x" + str(hashlib.shake_256(str(x[i, 4, 13]).encode()).hexdigest(4)),16)
    x[i, 5, 13] = int("0x" + str(hashlib.shake_256(str(x[i, 5, 13]).encode()).hexdigest(4)),16)
    for j in range(x.shape[1]):
        if math.isnan(x[i, j, 13]):
            x[i, j, 13] = 0

print("Normalizing...")
x_norm = (x - np.min(x)) / (np.max(x) - np.min(x))

print("Saving...")
np.save('../CapstoneData/x.npy',x_norm)