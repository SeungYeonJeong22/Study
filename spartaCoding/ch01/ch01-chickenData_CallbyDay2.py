#요일별 치킨 주문량 (주문량 순 정렬)
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'Malgun Gothic'       #한글 깨짐 방지 (window = Malgun Gothic / linux = 머 있는데 까먹음)

chicken07 = pd.read_csv('IndStudy/spartaCoding/data/chicken_07.csv')
chicken08 = pd.read_csv('IndStudy/spartaCoding/data/chicken_08.csv')
chicken09 = pd.read_csv('IndStudy/spartaCoding/data/chicken_09.csv')

# print(chicken07.head(3))
# print(chicken08.head(3))
# print(chicken09.head(3))


chicken_data = pd.concat([chicken07,chicken08,chicken09]).reset_index(drop=True)    #drop == index 삭제
# print(chicken_data)
# print(chicken_data.columns)
#요일별 주문량
call_data = chicken_data.groupby('요일').sum()['통화건수'].sort_values(ascending = False)

#Annotation을 위해 list에 데이터의 value값 저장
n = list(call_data.values)

plt.figure(figsize = (6,6))
plt.title('요일별 치킨 주문량 (주문량 순)')
plt.bar(call_data.index,call_data.values)   #x = 요일별 통화건수의 인덱스(요일) / y = value값(요일별 주문량)

for i, txt in enumerate(n):
    plt.annotate(txt,(call_data.index[i],call_data.values[i]))

plt.show()
