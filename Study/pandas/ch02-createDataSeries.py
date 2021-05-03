# import pandas as pd
#
# s1 = pd.Series({'김':100,'나':110,'박':124,'이':132})
# s1.name = '수학'
# print(s1)
# print('------------------')
#
# s2 = pd.Series({'김':10,'나':5,'박':123,'이':42})
# print(s2)
# print('------------------')
#
# s3 = pd.Series([8,3,12,2])
# s3.name = '국어'
# print(s3)
# print('------------------')
#
# s4 = pd.Series([30,5,123,423])
# print(s4)
# print('------------------')
#
# print("DataFrame Start")
#
# print('------------------')
# d1 = pd.DataFrame({'출생지':['한국','미국'],'나이':[25,30]})
# print(d1)
# print('------------------')
#
# d1['성별'] = ['여','남']
# print(d1)
# print('------------------')
#
# d1.loc[2] = ['일본','28','여']
# print(d1)
# print('------------------')
#
# print(d1.loc[1])
# print("d1.loc[1] type : ",type(d1.loc[1]))
# print('------------------')
#
# d2 = pd.DataFrame(s1)
# d2['영어'] = s2
# d2['미술'] = [1,2,3,4]
# print(d2)
# print('------------------')
import pandas as pd
import numpy as np

s1 = pd.Series({"김":100, "나":80, "박":96, "이":75})
s1.name = "국어"
print(s1)

print('--------------------------')
df = pd.DataFrame({'국어':[100,95],'영어':[95,88],'수학':[89,77]})

print(df)
print('--------------------------')
df['사회']= [80,55]
print(df)