N = int(input())
build = [0]
dp = [0] * (N +1)
for testCase in range(1,N+1):
    data = input()
    p = data.split()
    p = [int(i) for i in p]
    build.append(p)

    for i in range(0,len(build[testCase])-1):
        if i > 0:
            dp[testCase] += dp[build[testCase][i]]
    dp[testCase] += build[testCase][0]
    
for i in range(1,N+1):
    print(dp[i])