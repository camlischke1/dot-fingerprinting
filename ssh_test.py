import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tqdm import tqdm
import os
import math

path1 = "../CapstoneData/ssh_test.csv"        # assigning the csv file path
path2 = "../CapstoneData/tls_test.csv"        # assigning the csv file path
delta = .016241 + (2*0.006985)          # mean + 2std

'''
print("Writing ssh.csv file...")
command = "C:\\Progra~1\Wireshark\\tshark.exe -r ../CapstoneData/ssh_test.pcapng -Y ssh "\
         "-T fields -E header=y -E separator=, -E occurrence=f -E quote=n -e tcp.stream -e ip.src " \
          "-e _ws.col.Time -e _ws.col.Protocol > {}".format(path1)
os.system(command)
print("Writing tls.csv file...")
command = "C:\\Progra~1\Wireshark\\tshark.exe -r ../CapstoneData/ssh_test.pcapng -Y tls "\
         "-T fields -E header=y -E separator=, -E occurrence=f -E quote=n -e tcp.stream -e ip.src " \
          "-e _ws.col.Time -e _ws.col.Protocol -e tls.app_data > {}".format(path2)
os.system(command)
'''
print("Shaping ssh connections...")
ssh = pd.read_csv(path1)     # after creation of csv, read it into dataframe
ssh = ssh.sort_values(['tcp.stream'])
ssh = ssh.loc[ssh['_ws.col.Protocol'] == 'SSH']
print(ssh)


print("Shaping tls connections...")
tls = pd.read_csv(path2)
tls = tls.sort_values(['tcp.stream'])
tls = tls.loc[tls['tls.app_data'].notnull()]
tls = tls.loc[tls['ip.src'] == '192.168.126.122']
print(tls)

print("Collecting all matches...")
matches = []
for i in tqdm(range(len(tls))):
    low = tls.iloc[i]["_ws.col.Time"] - delta
    high = tls.iloc[i]["_ws.col.Time"] + delta
    matches.append(ssh.index[ssh['_ws.col.Time'].between(low,high)].tolist())


print("Testing matches...")

size = []
results_by_query = []
correct = 0
incorrect = 0
for i in tqdm(range(len(matches))):
    size.append(len(matches[i]))
    count = 0
    for j in range(len(matches[i])):
        if ssh.loc[matches[i][j]]["ip.src"] == "192.168.126.122":
            count += 1
    correct += count
    incorrect += len(matches[i]) - count
    if len(matches[i]) > 0:
        results_by_query.append(count/float(len(matches[i])))
    else:
        results_by_query.append(0)

print("Total correct mappings: ", correct)
print("Total incorrect mappings: ", incorrect)
print("Total SSH connections: ", correct + incorrect)
print("Accuracy: ", correct / (correct + incorrect))
df_describe = pd.DataFrame(results_by_query)
print(df_describe.describe())


