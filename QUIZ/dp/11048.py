N,M = map(int,input().split())
board = []
for i in range(N):
    board.append(list(map(int,input().split())))

t_board = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        t_board[i][j] = board[i-1][j-1] + max(t_board[i-1][j],t_board[i][j-1],t_board[i-1][j-1])

print(t_board[N][M])