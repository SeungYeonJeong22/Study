n = int(input())
p = [list(map(int,input().split())) for _ in range(n)]
t = p
for i in range(1,n):
    for j in range(len(p[i])):
        if j == 0:
            t[i][j] = t[i-1][j] + t[i][j]
        elif i == j:
            t[i][j] = t[i-1][j-1] + t[i][j]
        else:
            t[i][j] = max(t[i-1][j-1],t[i-1][j]) + t[i][j]
print(max(t[n-1]))