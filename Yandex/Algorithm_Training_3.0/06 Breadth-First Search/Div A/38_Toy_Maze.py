"""
Use BFS and add to the vertex from actions are made which are the last available if one made an action
"""
import sys
from collections import deque

DXY = [(1,0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
dist = [[float('inf') for _ in range(M)] for __ in range(N)]

q = deque()
dist[0][0] = 0
q.append((0, 0))

while len(q) != 0:
    x, y = q.popleft()
    for dx, dy in DXY:
        cur_x, cur_y = x, y
        while True:
            new_x = cur_x + dx
            new_y = cur_y + dy
            if 0 <= new_x < N and 0 <= new_y < M and field[new_x][new_y] != 1:
                cur_x, cur_y = new_x, new_y
            else:
                break
            if field[new_x][new_y] == 2:
                print(dist[x][y] + 1)
                sys.exit()

        if dist[cur_x][cur_y] > dist[x][y] + 1 and field[cur_x][cur_y] != 2:
            dist[cur_x][cur_y] = min(dist[cur_x][cur_y], dist[x][y] + 1)
            q.append((cur_x, cur_y))

ans = float('inf')
for i in range(N):
    for j in range(M):
        if field[i][j] == 2:
            ans = min(ans, dist[i][j])

print(ans)
'''
Performance: P 3.11.2 (101 ms, 4.39 Mb); P 3.9 PyPy 7.3.11 (221 ms, 28.09 Mb)
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