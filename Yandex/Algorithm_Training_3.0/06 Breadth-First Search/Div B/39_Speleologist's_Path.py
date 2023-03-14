"""
Use BFS
Note, for easier understanding solve as if first block is the lowest block and speleologist wants get to the end of cave
"""

def bfs(graph, start, path_len):
    graph[start[0]][start[1]][start[2]][0] = 0
    path_len[0].append((start[0], start[1], start[2]))

    for length in range(len(path_len)):
        for vertex in path_len[length]:
            i, j, k = vertex  # unpack the tuple
            # check all six possible options for neighbors
            if k-1 >= 0 and graph[i][j][k-1][1] == '.' and graph[i][j][k-1][0] == -1:
                path_len[length+1].append((i, j, k-1))
                graph[i][j][k-1][0] = length+1
            if k+1 < N and graph[i][j][k+1][1] == '.' and graph[i][j][k+1][0] == -1:
                path_len[length+1].append((i, j, k+1))
                graph[i][j][k+1][0] = length+1
            if j-1 >= 0 and graph[i][j-1][k][1] == '.' and graph[i][j-1][k][0] == -1:
                path_len[length+1].append((i, j-1, k))
                graph[i][j-1][k][0] = length+1
            if j+1 < N and graph[i][j+1][k][1] == '.' and graph[i][j+1][k][0] == -1:
                path_len[length+1].append((i, j+1, k))
                graph[i][j+1][k][0] = length+1
            if i-1 >= 0 and graph[i-1][j][k][1] == '.' and graph[i-1][j][k][0] == -1:
                path_len[length+1].append((i-1, j, k))
                graph[i-1][j][k][0] = length+1
            if i+1 < N and graph[i+1][j][k][1] == '.' and graph[i+1][j][k][0] == -1:
                path_len[length+1].append((i+1, j, k))
                graph[i+1][j][k][0] = length+1




# read input
N = int(input())

cave = [[[[-1, 'a'] for i in range(N)] for j in range(N)] for k in range(N)]  # [height][length][breadth]
start = ()
for i in range(N):
    input()  # empty string
    for j in range(N):
        line = input()
        for k in range(N):
            if line[k] == 'S':
                start = (i,j,k)
            cave[i][j][k][1] = line[k]

path_len = [[] for _ in range(N**3+1)]
bfs(cave, start, path_len)

# out of all possible paths' lengths to the lowest floor find minimum
ans = N**3 + 2
for j in range(N):
    for k in range(N):
        if cave[0][j][k][0] != -1:
            ans = min(ans, cave[0][j][k][0])

print(ans)

'''
Performance: P 3.11.2 (120 ms, 8.73 Mb); P 3.9 PyPy 7.3.11 (434 ms, 35.35 Mb)
Time complexity: O((N^3)^2)
Auxiliary Space: O(N^3)
Test Cases:
1

S
ans: 0
2

.#
##

..
.S
ans: 3
3

###
###
.##

.#.
.#S
.#.

###
...
###
ans: 6
'''