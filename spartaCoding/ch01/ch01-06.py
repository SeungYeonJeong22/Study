import pandas as pd
import matplotlib.pyplot as plt

chicken07 = pd.read_csv('SpartaCoding_JN/ch01/data/chicken_07.csv')
chicken08 = pd.read_csv('SpartaCoding_JN/ch01/data/chicken_08.csv')
chicken09 = pd.read_csv('SpartaCoding_JN/ch01/data/chicken_09.csv')

chicken_data = pd.concat([chicken07,chicken08,chicken09])
chicken_data = chicken_data.reset_index(drop = True)
print(chicken_data)

group_data = chicken_data.groupby('요일')
call_data = group_data['통화건수']
sum_data = call_data.sum()
print(sum_data)

plt.rcParams['font.family'] = 'Malgun Gothic'

# sorted_data = sum_data.sort_values(ascending = False)

weeks = ['월','화','수','목','금','토','일']
weeks_data = chicken_data.groupby('요일').sum()['통화건수'].reindex(weeks)

# plt.figure(figsize=(8,5))
# plt.bar(sum_data.index,sum_data.values)
# plt.title('요일별 통화건수의 합')
# plt.show()

# plt.figure(figsize=(8,5))
# plt.bar(sorted_data.index,sorted_data.values)
# plt.title('요일별 통화건수의 합')
# plt.show()

plt.figure(figsize=(8,5))
plt.bar(weeks_data.index,weeks_data)
plt.title('요일별 통화건수의 합')
plt.show()