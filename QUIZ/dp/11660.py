N,M = map(int,input().split())
p = [list(map(int,input().split())) for _ in range(N)]

for testCase in range(M):
    dp = [[0] * (N+1) for _ in range(N+1)]
    x1,y1,x2,y2 = map(int,input().split())
    
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if j == y1:
                dp[i][j] = p[i-1][j-1] + dp[i-1][y2]
            else:
                dp[i][j] = p[i-1][j-1] + dp[i][j-1]
        
    print(dp[x2][y2])