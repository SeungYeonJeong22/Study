t = [input() for _ in range(2)]
dp = []
for i in t[0]:
    idx = t[0].find(i)
    for j in range(idx,len(t[1])):
        if i == t[1][j]:
            dp.append(i)
            break

print(dp)
print(len(dp))