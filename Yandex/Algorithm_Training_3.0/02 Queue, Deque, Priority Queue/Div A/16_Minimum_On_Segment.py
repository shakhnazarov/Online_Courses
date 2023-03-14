"""
Use priority queue (MinHeap representation), also use the additional map to keep window items as doing new heap each
time is too expensive timewise
"""
import heapq
from collections import Counter


# read input
n, k = map(int, input().split())
line = list(map(int, input().split()))
window = line[:k]
window_items = Counter(window)
heapq.heapify(window)  # use MinHeap for the window
ans = []
for i in range(k, n):
    while window[0] not in window_items or window_items[window[0]] == 0:  # check if min from elements before window
        heapq.heappop(window)
    ans.append(window[0])
    heapq.heappush(window, line[i])
    window_items[line[i-k]] -= 1
    window_items[line[i]] = 1 + window_items.get(line[i], 0)

# last value does not calculate in the loop due to our realization
while window[0] not in window_items or window_items[window[0]] == 0:
        heapq.heappop(window)
ans.append(window[0])
print(*ans)

'''
Performance: P 3.11.2 (437 ms, 18.85 Mb); P 3.9 PyPy 7.3.11 (449 ms, 62.23 Mb)
Complexity: O(N*logN)  # each time we insert for logN (N as do note delete items and heap could be of size N)
Auxiliary space: O(N)
Test cases:
7 3
1 3 2 4 5 3 1
ans: 1 2 2 3 1
1 1
1
ans: 1
2 1
10 3
ans: 10 3
7 1
1 2 3 4 5 6 7
ans: 1 2 3 4 5 6 7
'''