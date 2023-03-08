"""
Each time we ask whether the number is in the first k numbers, then we may compute what is the best k to choose
Dynamics: minimum number of candy needed to guarantee finding the answer (does not matter what subset of numbers of N,
care only about the power (quantity) of the set
"""

# read input
N, a, b = map(int, input().split())

dp = [0 for i in range(N+2)]
dp[2] = max(a, b)
for i in range(3, N+1):
    temp_min = i*max(a,b)
    for k in range(1, i):
        # as worst case is considered, find the max between division of the set of numbers
        temp_min = min(temp_min, max(dp[k]+a, dp[i-k]+b))
    dp[i] = temp_min

print(dp[N])

'''
Complexity: O(N)
Auxiliary Space Complexity: O(N)
Test cases:
8 1 1
ans: 3
10 5 0
ans: 5
7 0 2
ans: 2
9 2 1
ans: 6
10 1 2
ans: 6
'''