import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tqdm import tqdm
import os
import math

path1 = "../CapstoneData/ssh.csv"        # assigning the csv file path
path2 = "../CapstoneData/tls.csv"        # assigning the csv file path
'''
print("Writing ssh.csv file...")
command = "C:\\Progra~1\Wireshark\\tshark.exe -r ../CapstoneData/ssh.pcapng -Y ssh "\
         "-T fields -E header=y -E separator=, -E occurrence=f -E quote=n -e tcp.stream -e ip.src " \
          "-e _ws.col.Time -e _ws.col.Protocol > {}".format(path1)
os.system(command)
print("Writing tls.csv file...")
command = "C:\\Progra~1\Wireshark\\tshark.exe -r ../CapstoneData/ssh.pcapng -Y tls "\
         "-T fields -E header=y -E separator=, -E occurrence=f -E quote=n -e tcp.stream -e ip.src " \
          "-e _ws.col.Time -e _ws.col.Protocol -e tls.app_data > {}".format(path2)
os.system(command)
'''
print("Shaping ssh connections...")
ssh = pd.read_csv(path1)     # after creation of csv, read it into dataframe
ssh = ssh.sort_values(['tcp.stream'])
ssh = ssh.loc[ssh['_ws.col.Protocol'] == 'SSH']
print(ssh)
print(len(ssh))


print("Shaping tls connections...")
tls = pd.read_csv(path2)
tls = tls.sort_values(['tcp.stream'])
tls = tls.loc[tls['tls.app_data'].notnull()]
tls = tls.loc[tls['ip.src'] == '192.168.126.122']
print(tls)
print(len(tls))


print("Mapping time differences...")
diff = []
for i in range(len(tls)):
    diff.append(ssh.iloc[i]["_ws.col.Time"] - tls.iloc[i]["_ws.col.Time"])
diff = np.round(np.array(diff),8)

fig, ax = plt.subplots(figsize=(10, 7))
ax.hist(diff, bins=2000)
plt.xlim([0, 0.171])
plt.show()

df_describe = pd.DataFrame(diff)
print(df_describe.describe())

Q1 = df_describe.quantile(0.25)
Q3 = df_describe.quantile(0.75)
IQR = Q3 - Q1
df_describe = df_describe[~((df_describe < (Q1 - 1.5 * IQR)) |(df_describe > (Q3 + 1.5 * IQR))).any(axis=1)]
fig, ax = plt.subplots(figsize=(10, 7))
ax.hist(np.array(df_describe), bins=200)
plt.xlim([0, 0.034])
plt.show()
print(df_describe.describe())
