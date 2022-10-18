# from keras.utils import to_categorical
import numpy as np
import hashlib
import math
from sklearn import preprocessing

x = np.load('../CapstoneData/dotsample.npy', allow_pickle=True)
y = np.load('../CapstoneData/y.npy', allow_pickle=True)
urls = np.load('../CapstoneData/urls.npy', allow_pickle=True)

# delete redundant data attributes
x = np.delete(x, 0, 2)      # source IP (covered by dest IP)
x = np.delete(x, 3, 2)      # ip.protocol is '6' for all packets
x = np.delete(x, 2, 2)      # IP ttl covered by source IP




# The headers below relate to the attributes in each of the captured packets.

# 0-ip.dest    1-ip.len   2-tcp.window_size   3-tcp.ack   4-tcp.seq
# 5-tcp.len   6-frame.time_relative   7-frame.time_delta     8-tcp.time_relative    9-tcp.time_delta
# 10-tls.record.content_type  11-_ws.col.Length   12-tls.record.length    13-tls.app_data

# make sourceIP into binary value of sent by client 64bytes(-1), sent by server 128bytes(1)
x = np.where(x == '192.168.126.122',1,x)    # destination is client IP
x = np.where(x == '192.168.126.131',-1,x)    # destination is server IP

# make make tls.record.content_type map to 0,1,2,3 respectively
x[:,:,9] = np.subtract(x[:,:,9],20)
x[:,:,9] = x[:,:,9].astype(int)

# convert tls.app_data (encrypted data string) to hash of 8 bytes and then convert hash to integer
for i in range(x.shape[0]):
    x[i, 4, 13] = int("0x" + str(hashlib.shake_256(str(x[i, 4, 13]).encode()).hexdigest(4)),16)
    x[i, 5, 13] = int("0x" + str(hashlib.shake_256(str(x[i, 5, 13]).encode()).hexdigest(4)),16)
    for j in range(x.shape[1]):
        if math.isnan(x[i, j, 13]):
            x[i, j, 13] = 0


x_norm = (x - np.min(x)) / (np.max(x) - np.min(x))
print(x.shape)
print(x_norm.shape)
np.save('../CapstoneData/dotsample_norm.npy',x_norm)
'''
# check to make sue the normalization process went well
print(str(np.unique(x[:,:,0]).shape) + "    " + str(np.unique(x_norm[:,:,0]).shape))
print(str(np.unique(x[:,:,1]).shape) + "    " + str(np.unique(x_norm[:,:,1]).shape))
print(str(np.unique(x[:,:,2]).shape) + "    " + str(np.unique(x_norm[:,:,2]).shape))
print(str(np.unique(x[:,:,3]).shape) + "    " + str(np.unique(x_norm[:,:,3]).shape))
print(str(np.unique(x[:,:,4]).shape) + "    " + str(np.unique(x_norm[:,:,4]).shape))
print(str(np.unique(x[:,:,5]).shape) + "    " + str(np.unique(x_norm[:,:,5]).shape))
print(str(np.unique(x[:,:,6]).shape) + "    " + str(np.unique(x_norm[:,:,6]).shape))
print(str(np.unique(x[:,:,7]).shape) + "    " + str(np.unique(x_norm[:,:,7]).shape))
print(str(np.unique(x[:,:,8]).shape) + "    " + str(np.unique(x_norm[:,:,8]).shape))
print(str(np.unique(x[:,:,9]).shape) + "    " + str(np.unique(x_norm[:,:,9]).shape))
print(str(np.unique(x[:,:,10]).shape) + "    " + str(np.unique(x_norm[:,:,10]).shape))
print(str(np.unique(x[:,:,11]).shape) + "    " + str(np.unique(x_norm[:,:,11]).shape))
print(str(np.unique(x[:,:,12]).shape) + "    " + str(np.unique(x_norm[:,:,12]).shape))
'''