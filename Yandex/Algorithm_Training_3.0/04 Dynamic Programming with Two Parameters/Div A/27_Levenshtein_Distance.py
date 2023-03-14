"""
Use DP
Dynamics: dp[i][j] shows the Levenshtein distance between strings of str_1[:i] and str_2[:j]
Step: compare what is the best strategy given the actions we have (delete, add, replace)
"""

# read input
str_1 = input()
str_2 = input()

dp = [[_ for _ in range(len(str_2)+1)] for _ in range(len(str_1)+1)]
for i in range(len(str_1)+1):
    dp[i][0] = i

for i in range(len(str_1)):
    for j in range(len(str_2)):
        same_letter = (str_1[i] == str_2[j])  # if the letter is the same we do not replace it
        dp[i+1][j+1] = 1 + min(dp[i][j] - same_letter, dp[i][j+1], dp[i+1][j])

print(dp[len(str_1)][len(str_2)])

'''
Performance: P 3.11.2 (Time Limit); P 3.9 PyPy 7.3.11 (240 ms, 33.46 Mb)
Complexity: O(N*M)  # N = len(str_1), M = len(str_2)
Auxiliary Space Complexity: O(N*M
Test cases:
ABCDEFGH
ACDEXGIH
ans: 3
A
A
ans: 0
A
B
ans: 1
SXA
XA
ans: 1
XA
SXA
ans: 1
'''
