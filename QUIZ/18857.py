V,E = input('input V,E : ').split(' ')
V = int(V)
E = int(E)

#목표와 연결된 간선
def func(X,Y,dest):
    node = []
    for i in Y:
        if i==dest:
            node.append(Y.index(i))

    for i in X:
        if i == dest:
            node.append(X.index(i))
    return node

print('X,Y,D input : ')
X = []
Y = []
D = []
node_index = []
for i in range(0,E):
    x,y,d = input().split(' ')
    X.append(int(x))
    Y.append(int(y))
    D.append(int(d))

node_index = func(X,Y,V)

# for i in node_index:
#     node_weight += D[func(X,Y,i)]

# print(node_weight)


#훈련소에 연결된 간선까지의 최단거리 삭제 - 삭제한 경로는 재생성x


#그 간선에 도달하는 최단 거리 확인

