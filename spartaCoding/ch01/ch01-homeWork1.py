#요일별 피자 주문량
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'Malgun Gothic'

pizza09 = pd.read_csv('IndStudy/SpartaCoding/data/pizza_09.csv')
# print(pizza09.columns)
weeks = ['월','화','수','목','금','토','일']
pizza_data = pizza09.groupby('요일').sum()['통화건수'].reindex(weeks)
# pizza_data = pizza09.groupby('요일').sum()['통화건수'].sort_values()

sum_val = list(pizza_data.values)

plt.figure('Pizza Data',figsize=(5,5))
plt.title('요일별 피자 주문량')
plt.bar(pizza_data.index,pizza_data.values)
for i,val in enumerate(sum_val):
    plt.annotate(val,(pizza_data.index[i],pizza_data.values[i]))
plt.show()