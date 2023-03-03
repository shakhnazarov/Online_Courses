"""
Use priority queue (MinHeap representation), also use the additional deque to keep window items as doing new heap each
time is too expensive timewise
"""
import heapq
from collections import deque

# read input
n, k = map(int, input().split())
line = list(map(int, input().split()))
window = line[:k]
window_items = deque(window)
heapq.heapify(window)  # use MinHeap for the window

for i in range(k, n):
    while window[0] not in window_items:  # check if min from elements before window
        heapq.heappop(window)

    print(window[0])
    heapq.heappush(window, line[i])
    window_items.popleft()
    window_items.append(line[i])

# last value does not print in the loop due to our realization
while window[0] not in window_items:
        heapq.heappop(window)
print(window[0])



'''
Complexity: O(n*k)  # each time we heapify for O(k)
Auxiliary space: O(k)
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