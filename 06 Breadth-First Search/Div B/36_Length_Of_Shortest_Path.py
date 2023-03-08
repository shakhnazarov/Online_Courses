"""
Use BFS to find all shortest distances within the component, if end is in component print out length
"""
import sys
sys.setrecursionlimit(100001)

def bfs(graph, paths, now):
    if len(paths[0]) == 0:  # initialize paths
        paths[0].append(now)

    for length in range(len(paths)):  # iterate over each possible distance
        for vertex in paths[length]:
            graph[vertex][0] = 2  # colorize the vertex to show that we have been here
            for neigh in graph[vertex][1]:
                if graph[neigh][0] == 0:  # do not visit already visited
                    paths[length+1].append(neigh)
                    graph[neigh][0] = 1


# read input
N = int(input())
# convert adjacency matrix to adjacency list; if color is 1 then vertex is in paths but not yet visited, 2 if visited
graph = [[0, []] for i in range(N+1)]  # [color, [neighs]]
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
print(ans_len)

'''
Complexity: O(V^2+E)  # O(V+E) BFS and O(V^2) for input
Auxiliary Space Complexity: O(V+E)
Test Cases:
3
0 1 1
1 0 1
1 1 0
1 3
ans: 1
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
ans: 2
5
0 1 0 0 1
1 0 1 0 0
0 1 0 0 0
0 0 0 0 0
1 0 0 0 0
3 5
ans: 3
'''
