"""
As knights move simultaneously then they will meet in //2 the initial distance between first and second knight and
will not meet if the distance is odd (imagine 2x3 board in which knights stay on opposite directions of the field)
Main concern that knights may do a workaround and change the parity but one can prove it is impossible
"""
def bfs(board, paths, start, length=0):
    if board[start[0]][start[1]][0] == -1:
        paths[length].append(start)
        board[start[0]][start[1]][0] = length
    for length in range(len(paths)):
        for cell in paths[length]:
            for neigh in board[cell[0]][cell[1]][1]:
                if board[neigh[0]][neigh[1]][0] == -1:
                    paths[length+1].append(neigh)
                    board[neigh[0]][neigh[1]][0] = length + 1


# read input
f_k, s_k = input().split()
map_letters = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
f_k = (int(f_k[1]), map_letters[f_k[0]])  # in chess format first col then row, reverse for algorithmic purposes
s_k = (int(s_k[1]), map_letters[s_k[0]])

# find neighbors (in knight-movement fashion) for each cell
N = M = 8
board = [[[-1,[]] for i in range(M+1)] for j in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        # overall 8 positions possible given constraints of the board are maintained
        if i-2 > 0 and j-1 > 0:
            board[i][j][1].append((i-2, j-1))
        if i-2 > 0 and j+1 <= M:
            board[i][j][1].append((i-2, j+1))
        if i-1 > 0 and j-2 > 0:
            board[i][j][1].append((i-1, j-2))
        if i+1 <= N and j-2 > 0:
            board[i][j][1].append((i+1, j-2))
        if i-1 > 0 and j+2 <= M:
            board[i][j][1].append((i-1, j+2))
        if i+1 <= N and j+2 <= M:
            board[i][j][1].append((i+1, j+2))
        if i+2 <= N and j-1 > 0:
            board[i][j][1].append((i+2, j-1))
        if i+2 <= N and j+1 <= M:
            board[i][j][1].append((i+2, j+1))

# find all possible paths from the first knight to any cell
paths = [[] for i in range(N*M+1)]
bfs(board, paths, f_k)

# as knights move simultaneously, if initial path's length is odd, they won't be able to meet
if board[s_k[0]][s_k[1]][0] % 2 == 1:
    print(-1)
else:
    print(board[s_k[0]][s_k[1]][0] // 2)
'''
Performance: P 3.11.2 (44 ms, 4.40 Mb); P 3.9 PyPy 7.3.11 (172 ms, 28.09 Mb)
Time complexity: O((N*M)^2)
Auxiliary space: O(N*M)
a1 a2
ans: -1
a1 a3
ans: 1
h1 a8
ans: 3
'''