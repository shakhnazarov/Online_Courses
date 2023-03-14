"""
Topological sort - naming of vertexes in such way that no vertex receives and edge from a vertex of higher number-name
Use dfs and colorize into 3 colors:
0 - white - we have not been in the vertex
1 - grey - we have been in the vertex but have not checked all the children yet
2 - black - we have been in the vertex and checked all the children
"""
import sys
sys.setrecursionlimit(100001)  # initial limit is usually 1000

def dfs(graph, now):
    global is_cycle
    graph[now][0] = 1
    for neigh in graph[now][1]:
        if graph[neigh][0] == 0:
            dfs(graph, neigh)
        elif graph[neigh][0] == 2:
            continue
        else:  # grey vertex
            is_cycle = True
    graph[now][0] = 2  # colorize in black when checked all neighs
    graph_sorted.append(now)


# read input
N, M = map(int, input().split())
graph = [[0, []] for i in range(N+1)]  # [color, [neighbors]]
for i in range(M):
    ver_1, ver_2 = map(int, input().split())
    graph[ver_1][1].append(ver_2)  # add one time as graph is oriented

# if there is a cycle in the graph then topsort is not possible
global is_cycle
is_cycle = False
graph_sorted = []
for i in range(1, N+1):
    if graph[i][0] == 0:
        dfs(graph, i)
    if is_cycle:
        break

# print out the answer
if is_cycle:
    print(-1)
else:
    print(*graph_sorted[::-1])  # in reverse order as initially we moved from children to parents)

'''
Performance: P 3.11.2 (-); P 3.9 PyPy 7.3.11 (650 ms, 37.45 Mb)
Time complexity: O(N+M)
Auxiliary Space: O(N+M)
Test cases:
6 6
1 2
3 2
4 2
2 5
6 5
4 6
ans: 4 6 1 2 5
2 1
1 2
ans: 1 2
3 3
1 2
2 3
3 1
ans: -1
'''

