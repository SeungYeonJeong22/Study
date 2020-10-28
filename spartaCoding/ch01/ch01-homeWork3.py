#요일별 치킨 & 피자 주문량 (요일순 정렬)
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.family'] = 'Malgun Gothic'       #한글 깨짐 방지
chicken09 = pd.read_csv('IndStudy/spartaCoding/data/chicken_09.csv')
pizza09  = pd.read_csv('IndStudy/spartaCoding/data/pizza_09.csv')

#요일별 주문량
weeks = ['월','화','수','목','금','토','일']

c_data = chicken09.groupby('요일').sum()['통화건수'].reindex(weeks)
p_data = pizza09.groupby('요일').sum()['통화건수'].reindex(weeks)

c_val = list(c_data.values)
p_val = list(p_data.values)

print('>>>>>c_data.values',type(c_data.values))
print('>>>>>c_val',c_val)
print('>>>>>c_val type : ',type(c_val))

plt.figure('chicken & pizza Data',figsize = (6,6))
plt.title('요일별 치킨 & 피자 주문량 (요일 순)')
plt.bar(c_data.index,c_data.values,color = 'orange')
plt.bar(p_data.index,p_data.values,color = 'blue')

for i,txt in enumerate(c_val):
    plt.annotate(txt,(c_data.index[i],c_data.values[i]))

for i,txt in enumerate(p_val):
    plt.annotate(txt,(p_data.index[i],p_data.values[i]))

plt.show()
