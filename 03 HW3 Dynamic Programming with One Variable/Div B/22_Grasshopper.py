# read input
N, k = map(int, input().split())

'''
Use DP approach
Step: if location is >> k then we can get there by ans(N-1) + ans(N-2) + ... + ans(N-k) as we can make a jump from
distance up to k from N. Take ans(N) - ans(N-1) = (ans(N-1) + ans(N-2) + ... + ans(N-k)) - 
(ans(N-2) + ans(N-3) + ... + ans(N-k-1)) = ans(N-1) - ans(N-k-1) => ans(N) = 2*ans(N-1) - ans(N-k-1)
Base: should calculate base for up to k cells, construct several elements to see a pattern
1 - 1 #1
2 - 11 2 #2
3 - 111 21 12 3 #4
4 - 1111 211 121 211 22 31 13 4 #8
5 - 11111 2111 1211 1121 1112 221 212 122 311 131 113 32 23 41 14 5 #16
seems as if 2**(N-1) (can prove by induction)
'''

# to not calculate base case by hand, prefill the dp array
dp = [0, 1] # first element will be zero, just to keep numeration consistent, we can do nothing by exactly 1 way

for i in range(2, k+2):
    dp.append(2**(i-2))
dp.append(2**k - 1)  # now we cannot jump from 1 to k+2 using th ejump of lenght k (sum of previous k terms)
for i in range(k+3, N+1):
    dp.append(2*dp[i-1] - dp[i-k-1])


print(dp[N])

'''
Complexity: O(N)
Auxiliary Space: O(N)
Test cases:
4 8
ans: 4
8 2
ans: 21
1 1
ans: 1'''