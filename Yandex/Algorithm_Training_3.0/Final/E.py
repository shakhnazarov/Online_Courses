
import sys
from collections import deque

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0), (1,1), (-1, 1), (-1,-1), (1,-1)]

# Read input
h, w = map(int, input().split())
grid = [input().strip() for _ in range(h)]
sx, sy = map(int, input().split())
tx, ty = map(int, input().split())
start = (h-sy, sx-1)
target = (h-ty, tx-1)

dist = [[float('inf') for _ in range(w)] for __ in range(h)]

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
            if 0 <= new_x < h and 0 <= new_y < w and grid[new_x][new_y] != 'X':
                cur_x, cur_y = new_x, new_y
            else:
                break
            if (new_x, new_y) == target:
                print(dist[x][y] + 1)
                sys.exit()

        if dist[cur_x][cur_y] > dist[x][y] + 1 and (cur_x, cur_y) != target:
            dist[cur_x][cur_y] = min(dist[cur_x][cur_y], dist[x][y] + 1)
            q.append((cur_x, cur_y))

ans = h*w*w*h
for i in range(h):
    for j in range(w):
        if (i, j) == target:
            ans = min(ans, dist[i][j])

if ans == h*w*w*h:
    print(-1)
else:
    print(ans)