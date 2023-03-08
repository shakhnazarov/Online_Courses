"""
as number of actions to sum up N numbers is N-1 then we want to get the minimal sum of two numbers. Thus, keep MinHeap
and sum up the 2 smallest number
"""
import heapq

# read input
N = int(input())
nums = list(map(int, input().split()))
sums = 0
heapq.heapify(nums)

while len(nums) > 1:
    sum_temp = heapq.heappop(nums) + heapq.heappop(nums)
    sums += sum_temp
    heapq.heappush(nums, sum_temp)

print(f'{round(0.05*sums, 2):.2f}')  # need to fix output at 2 decimal places

'''
Complexity: O(NlogN)
Auxiliary Space: O(1)
Test cases:
4
10 11 12 13
ans: 4.60
2
1 1
ans: 0.10
6
1 2 3 4 5 6
ans: 2.55
'''