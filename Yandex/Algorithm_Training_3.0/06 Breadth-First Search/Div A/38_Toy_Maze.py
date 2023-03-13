"""
Use BFS and add to the vertex from actions are made which are the last available if one made an action
"""
def bfs(graph, paths):
    for length in range(len(paths)):
        for vertex in paths[length]:
            i_init, j_init = vertex

            # rotate towards ourselves
            i = i_init + 1
            j = j_init
            while i < N:
                if graph[i][j][2] == 2:
                    return length+1
                elif graph[i][j][2] == 1:
                    break
                elif graph[i][j][2] == 0 and graph[i][j][1] != 1:  # do not update for rotating
                    graph[i][j][0] = length+1
                i += 1
            field[i-1][j][1] = 1  # reached end
            if (i-1, j) not in paths[length]:  # check whether the same vertex
                paths[length+1].append((i-1, j))

            # rotate outwards
            i = i_init - 1
            j = j_init
            while i > -1:
                if graph[i][j][2] == 2:
                    return length + 1
                elif graph[i][j][2] == 1:
                    break
                elif graph[i][j][2] == 0 and graph[i][j][1] != 1:  # do not update for rotating
                    graph[i][j][0] = length + 1
                i -= 1
            field[i + 1][j][1] = 1  # reached end
            if (i + 1, j) not in paths[length]:
                paths[length+1].append((i + 1, j))

            # tilt left
            i = i_init
            j = j_init - 1
            while j > -1:
                if graph[i][j][2] == 2:
                    return length + 1
                elif graph[i][j][2] == 1:
                    break
                elif graph[i][j][2] == 0 and graph[i][j][1] != 1:  # do not update for rotating
                    graph[i][j][0] = length + 1
                j -= 1
            field[i][j+1][1] = 1  # reached end
            if (i, j+1) not in paths[length]:
                paths[length+1].append((i, j+1))

            # tilt right
            i = i_init
            j = j_init + 1
            while j < M:
                if graph[i][j][2] == 2:
                    return length + 1
                elif graph[i][j][2] == 1:
                    break
                elif graph[i][j][2] == 0 and graph[i][j][1] != 1:  # do not update for rotating
                    graph[i][j][0] = length + 1
                j += 1
            field[i][j - 1][1] = 1  # reached end
            if (i, j - 1) not in paths[length]:
                paths[length+1].append((i, j - 1))



# read input
N, M = map(int, input().split())
field = [[[-1, -1, -1] for _ in range(M)] for _ in range(N)]  # [length of path till point, can rotate from this, type]
field[0][0][0] = 0
field[0][0][1] = 1  # can rotate from this
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        field[i][j][2] = line[j]

paths = [[] for _ in range(N*M+1)]
paths[0].append((0,0))
print(bfs(field, paths))
'''
Complexity: O((M*N)^2)
Auxiliary Space Complexity: O(M*N)
Test Cases:
1 2
0 2
ans: 1
2 2
0 0
0 2
ans: 2
4 5
0 0 0 0 1
0 1 1 0 2
0 2 1 0 0
0 0 1 0 0
ans: 3
'''