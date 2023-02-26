"""
Use DP for solution
Step: for new num check among those subsequences which end with number less than the num and use the longest
Base:  no
"""

# read input
N = int(input())
nums = list(map(int,input().split()))

dp = [1]*N  # length of subsequence
indices = [-1]*N  # use index of the chosen number for continuation of subsequence (-1 if new subsequence)
ans_index = 0
for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1
            indices[i] = j

    # memorizes the max dp
    if dp[i] > dp[ans_index]:
        ans_index = i

# Recover subsequence
subsequence = [nums[ans_index]]
index_recover = ans_index
while indices[index_recover] != -1:
    subsequence.append(nums[indices[index_recover]])
    index_recover = indices[index_recover]

print(*subsequence[::-1])
'''
Complexity: O(N^2)
Auxiliary space: O(N)
Test cases:
4
1 1 1 1
ans: 1
6
3 29 5 5 28 6
ans: 3 5 28
10
4 8 2 6 2 10 6 29 58 9
ans: 4 8 10 29 58 
'''