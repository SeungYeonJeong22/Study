#greedy ATM
N = int(input())
p = list(map(int,input().split()))

if N == 1:
    print(p[0])
else:
    p.sort()

    time = 0   #time
    min_sum_t = 0   #minimum sum time

    for i in range(N):
        min_sum_t += (time + p[i])
        time += p[i]

    print(min_sum_t)
