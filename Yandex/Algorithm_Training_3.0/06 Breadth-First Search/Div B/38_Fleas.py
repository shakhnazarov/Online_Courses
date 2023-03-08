"""
We can find all possible ways from the feeder and then get answers for each request for O(1)
"""
def bfs(field, paths, start, length=0):
    if field[start[0]][start[1]][0] == -1:
        paths[length].append(start)
        field[start[0]][start[1]][0] = length
    for length in range(len(paths)):
        for cell in paths[length]:
            for neigh in field[cell[0]][cell[1]][1]:
                if field[neigh[0]][neigh[1]][0] == -1:
                    paths[length+1].append(neigh)
                    field[neigh[0]][neigh[1]][0] = length + 1


# read input
N, M, S, T, Q = map(int, input().split())
field = [[[-1,[]] for i in range(M+1)] for i in range(N+1)]
# find neighbors (in horse-movement fashion) for each cell
for i in range(1, N+1):
    for j in range(1, M+1):
        # overall 8 positions possible given constraints of the field are maintained
        if i-2 > 0 and j-1 > 0:
            field[i][j][1].append((i-2, j-1))
        if i-2 > 0 and j+1 <= M:
            field[i][j][1].append((i-2, j+1))
        if i-1 > 0 and j-2 > 0:
            field[i][j][1].append((i-1, j-2))
        if i+1 <= N and j-2 > 0:
            field[i][j][1].append((i+1, j-2))
        if i-1 > 0 and j+2 <= M:
            field[i][j][1].append((i-1, j+2))
        if i+1 <= N and j+2 <= M:
            field[i][j][1].append((i+1, j+2))
        if i+2 <= N and j-1 > 0:
            field[i][j][1].append((i+2, j-1))
        if i+2 <= N and j+1 <= M:
            field[i][j][1].append((i+2, j+1))

# find all possible paths from the feeder
paths = [[] for i in range(N*M+1)]
bfs(field, paths, (S, T))

# now we store the shortest pass from any cell to the feeder or keep -1 if there is no one
ans = 0
is_possible = True
for i in range(Q):
    row, col = map(int, input().split())
    if field[row][col][0] == -1:
        is_possible = False
        break
    else:
        ans += field[row][col][0]

# print out the answer
if is_possible:
    print(ans)
else:
    print(-1)

'''
Time complexity: O(Q(N*M)^2)
Auxiliary space: O(N*M)
Test cases:
2 2 1 1 1
2 2
ans: -1
2 2 1 1 1
1 1
ans: 0
4 4 1 1 16
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4
ans: 42
'''