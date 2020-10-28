# import pandas as pd

# pm_data = pd.read_csv("C:/Users/user/IndProj/IndStudy/Study/pandas/lab02_poketmon/poketmon_data.txt",header = None)
# pm_idx = pd.read_csv("C:/Users/user/IndProj/IndStudy/Study/pandas/lab02_poketmon/poketmon_index.txt",header = None)

# res = {}
# for tmp in pm_idx[0].values:
#     res[tmp] = 0

# for tmp in pm_data[0].values:
#     if tmp in res:
#         res[tmp]+=1

# print(res)

import pandas as pd

pm_indx = pd.read_csv("C:/Users/user/IndProj/IndStudy/Study/pandas/lab02_poketmon/poketmon_index.txt",header = None)
pm_data = pd.read_csv("C:/Users/user/IndProj/IndStudy/Study/pandas/lab02_poketmon/poketmon_data.txt",header = None)

res = {}
for tmp in pm_indx[0].values:
    res[tmp] = 0

print(pm_data[0].keys)

for tmp in pm_data[0].values:
    if tmp in res:
        res[tmp]+=1

# print(res)