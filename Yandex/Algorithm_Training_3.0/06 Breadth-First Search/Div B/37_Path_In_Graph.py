"""
Use BFS to find all shortest distances within the component, if end is in component print out length.
To recover answer just go from the element with length=l to l-1
"""
import sys
sys.setrecursionlimit(100001)

def bfs(graph, paths, now, length = 0):
    if len(paths[0]) == 0:  # initialize paths
        paths[0].append(now)

    for length in range(len(paths)):
        for vertex in paths[length]:
            graph[vertex][0] = 2
            for neigh in graph[vertex][1]:
                if graph[neigh][0] == 0:
                    paths[length+1].append(neigh)
                    graph[neigh][0] = 1


# read input
N = int(input())
# convert adjacency matrix to adjacency list
graph = [[0, []] for i in range(N+1)]  # [color, [neighs]] if color is 1 then vertex is in paths, 2 if visited
for i in range(1, N+1):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 1:
            graph[i][1].append(j+1)
start, end = map(int, input().split())

# Use BFS
paths = [[] for _ in range(N+1)]  # [vertexes] such that length of path from start to them equals to index
bfs(graph, paths, start)
ans_len = -1
for length, vertexes in enumerate(paths):
    if ans_len != -1:
        break
    for vertex in vertexes:
        if vertex == end:
            ans_len = length
            break

# Recover answer
path = [end]
l = ans_len
while l > 0:  # do not check for l in {-1, 0}
    for neigh in graph[end][1]:
        if neigh in paths[l-1]:  # need any neighbor with length == l-1
            path.append(neigh)
            end = neigh
            break
    l -= 1


print(ans_len)
if ans_len not in {0, -1}:
    print(*path[::-1])
'''
Performance: P 3.11.2 (55 ms, 4.41 Mb); P 3.9 PyPy 7.3.11 (225 ms, 28.10 Mb)
Complexity: O(V^2+E)  # O(V+E) BFS and O(V^2) for input
Auxiliary Space Complexity: O(V+E)
Test Cases:
3
0 1 1
1 0 1
1 1 0
1 3
ans: 1 1 3
4
0 0 1 0
0 0 0 1
1 0 0 0
0 1 0 0
1 2
ans: -1
10
0 1 0 0 0 0 0 0 0 0
1 0 0 1 1 0 1 0 0 0
0 0 0 0 1 0 0 0 1 0
0 1 0 0 0 0 1 0 0 0
0 1 1 0 0 0 0 0 0 1
0 0 0 0 0 0 1 0 0 1
0 1 0 1 0 1 0 0 0 0
0 0 0 0 0 0 0 0 1 0
0 0 1 0 0 0 0 1 0 0
0 0 0 0 1 1 0 0 0 0
5 4
ans: 2 5 2 4
5
0 1 0 0 1
1 0 1 0 0
0 1 0 0 0
0 0 0 0 0
1 0 0 0 0
3 5
ans: 3 2 1 5
1
0
1 1
ans: 0
'''
