t = int(input())
# nCm 이용 Combination
# n! // m! * (n-m)!

def facto(tmp):
    res = 1
    for a in range(tmp,0,-1):
        res *= a
    return res

# for _ in range(t):

for _ in range(t):
    n,m = map(int,input().split())
    if n == m:
        res = 1
    else:
        res = facto(m) // (facto(n) * facto(m-n))

    print(res)
