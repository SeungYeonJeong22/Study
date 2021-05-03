N,M = input('N M : ').split()
# N,M = map(int,input().split())
N = int(N)
M = int(M)
tryCnt = 0

r_p = []
b_p = []
g_p = ()
init_board = []
board = []

for a in range(N):
    tmp_board = []
    tmp = input()
    for b in range(M):
        tmp_board = list(tmp)
    board.append(tmp_board)
    if 'R' in tmp_board:
        r_p = [a,tmp_board.index('R')]
    if 'B' in tmp_board:
        b_p = [a,tmp_board.index('B')]
    if 'O' in tmp_board:
        g_p = (a,tmp_board.index('O'))

init_board = board

print('board : ',board)
print('r_p : ',r_p ,'b_p  : ',b_p,'g_p : ',g_p)
#.O으로 갈 수 있는 방향으로 가고 / 방금 왔던 방향으로의 기울기는 금지 / RB#이면 서로 못움직이게끔
#판 자체를 기울이며 두 개의 공이 동시에 움직인다

r_cur_pos = r_p
b_cur_pos = b_p
pre_dir = 0

def findRoot(cur_pos):
    global pre_dir
    availableRoot = [0,0,0,0]
    print('cur_pos : ',cur_pos)
    #init_board[y][x]
    if init_board[cur_pos[0]+1][cur_pos[1]] == '.' and not pre_dir == 'up':
        availableRoot[0] = 1
        pre_dir = 'down'
    if init_board[cur_pos[0]-1][cur_pos[1]] == '.' and not pre_dir == 'down':
        availableRoot[1] = 1 
        pre_dir = 'up'
    if init_board[cur_pos[0]][cur_pos[1]+1] == '.' and not pre_dir == 'left':
        availableRoot[2] = 1 
        pre_dir = 'right'
    if init_board[cur_pos[0]][cur_pos[1]-1] == '.' and not pre_dir == 'right':
        availableRoot[3] = 1
        pre_dir = 'left'

    print('dir : ',pre_dir)
    print('availableRoot : ',availableRoot)
    return availableRoot

def move(r_cur_pos,b_cur_pos,direction):
    if direction == 0:
        while not (init_board[r_cur_pos[0]+1][r_cur_pos[1]]=='#' or init_board[r_cur_pos[0]+1][r_cur_pos[1]]=='R' or init_board[r_cur_pos[0]+1][r_cur_pos[1]]=='B'):
            r_cur_pos[0] += 1
            if r_cur_pos == g_p:
                return
    elif direction == 1:
        while not (init_board[r_cur_pos[0]-1][r_cur_pos[1]]=='#' or init_board[r_cur_pos[0]-1][r_cur_pos[1]]=='R' or init_board[r_cur_pos[0]-1][r_cur_pos[1]]=='B'):
            r_cur_pos[0] -= 1
            if r_cur_pos == g_p:
                return
    elif direction == 2:
        while not (init_board[r_cur_pos[0]][r_cur_pos[1]+1]=='#' or init_board[r_cur_pos[0]][r_cur_pos[1]+1]=='R' or init_board[r_cur_pos[0]][r_cur_pos[1]+1]=='B'):
            r_cur_pos[1] += 1
            if r_cur_pos == g_p:
                return            
    elif direction == 3:
        while not (init_board[r_cur_pos[0]][r_cur_pos[1]-1]=='#' or init_board[r_cur_pos[0]][r_cur_pos[1]-1]=='R' or init_board[r_cur_pos[0]][r_cur_pos[1]-1]=='B'):
            r_cur_pos[1] -= 1
            if r_cur_pos == g_p:
                return            

for a in range(10):
    tryCnt += 1
    r_movable = findRoot(r_cur_pos)
    b_movable = findRoot(b_cur_pos)
    print('direction : ', r_movable.index(1))
    print('direction : ', b_movable.index(1))
    direction = r_movable.index(1)

    move(r_cur_pos,b_cur_pos,direction)
    if r_cur_pos == g_p:
        print('시도 횟수 : ',tryCnt)
        exit(0)

print('10번안에 찾기 실패')
print('-1')
