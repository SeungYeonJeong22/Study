import pandas as pd
import matplotlib.pyplot as plt

data_07 = pd.read_csv('SpartaCoding_JN/ch01/data/chicken_07.csv')
data_08 = pd.read_csv('SpartaCoding_JN/ch01/data/chicken_08.csv')
data_09 = pd.read_csv('SpartaCoding_JN/ch01/data/chicken_09.csv')

print(data_07.head(3))
print('------------------------------------------------------------------------')
print(data_08.head(3))
print('------------------------------------------------------------------------')
print(data_09.head(3))
print('------------------------------------------------------------------------')
print('------------------------------------------------------------------------')
print('------------------------------------------------------------------------')

con_data = pd.concat([data_07,data_08,data_09])
print('------------------------------------------------------------------------')
print('------------------------------------------------------------------------')
print('------------------------------------------------------------------------')
con_data = con_data.reset_index(drop=True)
print('con_data\n',con_data)

weeks = ['월','화','수','목','금','토','일']

#DataFrameGroupby,SeriesGroupby 는 뒤에 reindex를 할 수 없음
#묶어놓은거에서 집계함수(aggregation funcion)을 한 후에 Series로 형태를 변환해서 reindexing
print(dir(con_data))
group_day_data = con_data.groupby('요일')
call_data = group_day_data['통화건수']
sum_call_data = call_data.sum().reindex(weeks)
print('>>>>>sum_call_data<<<<<<\n',type(sum_call_data))
print('>>>>>sum_call_data<<<<<<\n',sum_call_data)

plt.rcParams['font.family'] = 'Malgun gothic'

plt.figure(figsize = (4,4))
plt.bar(sum_call_data.index,sum_call_data.values)
plt.show()
