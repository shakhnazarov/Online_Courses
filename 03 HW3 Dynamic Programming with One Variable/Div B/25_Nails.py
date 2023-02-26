"""
Use DP for solution
Step: in sorted array with the addition of new nail we must add new string from last nail to the one before last,
however: (Lent X -  be nail, O - Nth new nail, --- string)
-X          N-2
-X---X      N-1
-X---X---0  N
we may rearrange with additional N as either:
-X---X---0  OR
-X   X---0
thus, needed to compare such cases
Base: for first 2 cases
Dynamics: minimum length of string between i first in ascending order nails
"""

# read input
N = int(input())
nails = list(map(int, input().split()))
nails.sort()
dp = [nails[1]-nails[0], nails[1]-nails[0]]  #first element equals second to correctly compute 3rd
for i in range(2, N):
    dp.append(nails[i] - nails[i-1] + min(dp[i-1], dp[i-2]))

print(dp[N-1])

'''
Complexity: O(NlogN)
Auxiliary Space: O(N)
Test cases:
6
1 2 3 4 5 6
ans: 3
6
3 13 12 4 14 6
ans: 5
2
12 42
ans: 30'''