#군 별 피자 주문량
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'Malgun Gothic'

pizza09 = pd.read_csv('IndStudy/SpartaCoding/data/pizza_09.csv')
# print(pizza09.columns)
pizza_data = pizza09.groupby('발신지_구').sum()['통화건수'].sort_values(ascending = True)

sum_val = list(pizza_data.values)

plt.figure('Pizza Data',figsize=(20,5))
plt.title('지역별 피자 주문량')
plt.bar(pizza_data.index,pizza_data.values)
plt.xticks(rotation = 30)
for i,val in enumerate(sum_val):
    plt.annotate(val,(pizza_data.index[i],pizza_data.values[i]))
plt.show()