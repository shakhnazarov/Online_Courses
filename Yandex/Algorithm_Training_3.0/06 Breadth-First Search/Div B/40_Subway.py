"""
As distance between stations of the same line is essentially zero, treat lines as if they were vertexes
"""
def bfs(graph, len_paths):
    for length in range(len(len_paths)):
        for vertex in len_paths[length]:
            for neigh in graph[vertex][1]:
                if graph[neigh][0] == -1:
                    graph[neigh][0] = length+1
                    paths[length+1].append(neigh)

# Read input
N = int(input())
M = int(input())
lines = [[] for _ in range(M)]
for i in range(M):
    lines[i] = list(map(int,input().split()))[1:]
A, B = map(int, input().split())

# construct graph by adjacency list from lines (vertex is a line)
graph = [[-1, []] for i in range(M)]
for i in range(M):
    for station in lines[i]:
        for j in range(M):
            if i != j and (station in lines[j]):  # check if station in our line is also a station in other lines
                graph[i][1].append(j)

# find which lines contain A and B
lines_B = []
paths = [[] for _ in range(M+2)]
for i in range(M):
    if A in lines[i]:
        paths[0].append(i)  # simultaneously start from several points
        graph[i][0] = 0
    if B in lines[i]:
        lines_B.append(i)

# use bfs
bfs(graph, paths)

# find the shortest distance to any B
ans = -1
for length in range(len(paths)):
    if ans != -1:
        break
    for B in lines_B:
        if B in paths[length]:
            ans = length
            break

print(ans)

'''
Time Complexity: O(M^2*N)
Auxiliary Space: O(M^2)
Test cases:
5
2
4 1 2 3 4
2 5 3
3 1
ans: 0
5
2
4 1 2 3 4
1 5
3 5
ans: -1
2
1
2 1 2
2 1
ans: 0
2
2
1 1
1 2
1 2
ans: -1
'''

