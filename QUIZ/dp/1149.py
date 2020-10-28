# N = int(input())

# house = []
# for _ in range(N):
#     house.append(list(map(int,input().split(' '))))

# min_cost = -1
# min_indx = -1
# dp = []

# #제일 작은 값의 익덱스 와 그 전 집에 대해 가장 작은 값의 인덱스가 같으면 그 다음 최솟 값
# for i in range(len(house)):
#     #이전의 min_idx값과 현 min_indx 값이 같을 경우 그 다음 최솟값으로 설정
#     if min_indx == i.index(min(i)):
#         i.remove(min(i))
#         min_indx = i.index(min(i))
#     else: 
#         min_indx = i.index(min(i))
#     min_cost = i[min_indx]
#     dp.append(min_cost)

# print(sum(dp))


################################################################################
N = int(input())
house = []
for i in range(N):
    house.append(list(map(int,input().split(' '))))

for i in range(1,len(house)):
    house[i][0] = min(house[i-1][1],house[i-1][2]) + house[i][0]
    house[i][1] = min(house[i-1][0],house[i-1][2]) + house[i][1]
    house[i][2] = min(house[i-1][0],house[i-1][1]) + house[i][2]

print(min(house[N-1][0],house[N-1][1],house[N-1][2]))