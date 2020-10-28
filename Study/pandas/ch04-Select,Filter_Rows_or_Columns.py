import pandas as pd
import numpy as np

#요건 diction
friend_dict = {
    'name':['John','Jenny','Nate'],
    'age':[25,30,35],
    'job':['student','developer','teacher']
}

#요건 리스트
friend_list = [
    ['name',['John','Jenny','Nate']],
    ['age',[25,30,35]],
    ['job',['student','developer','teacher']]
]
df = pd.DataFrame.from_dict(friend_dict)
print(df[1:3])
print("--------------------------------")
df.loc[[0]]
print(df)
print("--------------------------------")
df = df[1:3]
print(df)

# df = pd.DataFrame.from_dict(friend_list)
# print(df)