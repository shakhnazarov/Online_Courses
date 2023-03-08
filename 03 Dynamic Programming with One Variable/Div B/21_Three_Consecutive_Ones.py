# read input
N = int(input())

'''
use DP for solution:
Step: We can add 1 or 0 to the sequences for N-1, thus ans(N) = 2*ans(N-1) but we should exclude sequences with 
last digits 011 which can be calculated as ans(N-4) (xxxxxx sequence of length N-4, xxxxxx011 sequence of length N-1). Hence,
ans(N)=2*ans(N-1) - ans(N-4)
Base: need to calculate for 0, 1, 2, 3
'''
dp = []
dp.append(2) # 0, 1
dp.append(4) # 00, 01, 10, 11
dp.append(7) # 000, 001, 010, 011, 100, 101, 110
dp.append(13) # 0000, 0001, 0010, 0011, 0100, 0101, 0110, 1000, 1001, 1010, 1011, 1100, 1101
for i in range(4, N):
    dp.append(2*dp[i-1] - dp[i-4])

# print out the last element of the dynamics
print(dp[N-1])  # does not work for N=0

'''
Complexity: O(NlogN) # for big numbers addition is O(logN), not O(1)
Auxiliary space: O(N)
Test cases:
1
ans: 2
4
ans: 13
5
ans: 24
'''