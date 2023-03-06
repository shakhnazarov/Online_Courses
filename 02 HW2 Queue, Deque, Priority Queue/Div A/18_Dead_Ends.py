"""
Use MinHeap to keep times of departure
"""
import heapq
# read input
K, N = map(int, input().split())
ans = []
dead_ends = [0 for _ in range(K)]

for i in range(N):
    arrival, departure = map(int, input().split())
    