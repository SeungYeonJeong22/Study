#요일별 치킨 주문량 (요일순 정렬)
import matplotlib.pyplot as plt
import pandas as pd

chicken07 = pd.read_csv('IndStudy/spartaCoding/data/chicken_07.csv')
chicken08 = pd.read_csv('IndStudy/spartaCoding/data/chicken_08.csv')
chicken09 = pd.read_csv('IndStudy/spartaCoding/data/chicken_09.csv')

# print(chicken07.head(3))
# print(chicken08.head(3))
# print(chicken09.head(3))

chicken_data = pd.concat([chicken07,chicken08,chicken09]).reset_index(drop=True)
# print(chicken_data)
# print(chicken_data.columns)
#요일별 주문량
weeks = ['월','화','수','목','금','토','일']

# call_data = chicken_data.groupby('요일').sum()['통화건수'].reindex(weeks)

week = chicken_data.groupby('요일') #type = padnas.core.groupby.generic.DataFrameGroupby object
sum_data = week.sum()               #week로 모은 dataframe에서 int형만 집계한 변수
call_data = sum_data['통화건수'].reindex(weeks)    #요일별 통화건수의 총합 / reindexing까지

plt.rcParams['font.family'] = 'Malgun Gothic'       #한글 깨짐 방지 (window = Malgun Gothic / linux = 머 있는데 까먹음)

plt.figure(figsize = (6,6))
plt.title('요일별 치킨 주문량 (요일 순)')
plt.bar(call_data.index,call_data.values)   #x = 요일별 통화건수의 인덱스(요일) / y = value값(요일별 주문량)
plt.show()
