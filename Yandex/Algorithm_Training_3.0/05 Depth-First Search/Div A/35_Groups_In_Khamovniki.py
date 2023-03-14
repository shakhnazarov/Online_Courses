"""
Use TopSort to find the order, note that we need to find a specific order not just any. Start from the end of the
graph (i.e. from groups which do not serve as a prerequisite to anything) and chose the maximum available then update
the set of vertexes you are choosing from
"""
import heapq

# read input
N = int(input())
graph = [set() for i in range(N+1)]
graph_inverted = [[] for _ in range(N+1)]
for i in range(1, N+1):
    line = list(map(int, input().split()))
    for j in range(1, len(line)):
        graph[line[j]].add(i)
        graph_inverted[i].append(line[j])

last_heap = []
for i in range(1, N+1):
    if len(graph[i]) == 0:
        heapq.heappush(last_heap, -1*i)  # -1 as heapq is a realization of MinHeap

ans = []
for i in range(1, N+1):
    vert = -1*heapq.heappop(last_heap)
    ans.append(vert)
    for neigh in graph_inverted[vert]:  # check whether any vertexes that were prerequisites to the given became last
        graph[neigh].remove(vert)
        if len(graph[neigh]) == 0:
            heapq.heappush(last_heap, -1*neigh)

# print out the reversed result
print(*ans[::-1])

'''
Performance: P 3.11.2 (885 ms, 48.52 Mb); P 3.9 PyPy 7.3.11 (713 ms, 75.52 Mb)
Complexity: O(NlogN + M)  # M is number of edges
Auxiliary Space: O(N + M)
Test Cases:
6
1 2
0
1 2
3 1 2 5
1 2
4 1 3 4 5
ans: 2 1 3 5 4 6
5
0
1 1
1 5
1 2
1 2
ans: 1 2 5 3 4
'''




