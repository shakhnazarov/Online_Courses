"""
Use DP
Dynamics: the length of the biggest common subsequence for first i elements of first and j elements of second
Step: if i and j elements of sequences are equal then we can add them to the commnon subsequence and choose
max(dp[i-1][j], dp[i][j-1) and add 1 or just choose the max
Note, mentally construct second sequence along the columns and first along the rows, e.g.:
~   a   b   c
b   0   1   1
c   0   1   2
a   1   1   2
"""

# read input
N = int(input())
f_s = list(map(int, input().split()))
M = int(input())
s_s = list(map(int, input().split()))

dp = [[0]*(M+1) for x in range(N+1)]  # extra 0 row, column to use recurrency from the beginning
for i in range(1, N+1):
    for j in range(1, M+1):
        if f_s[i-1] == s_s[j-1]:  # numeration for pd and sequences is different
            dp[i][j] = 1 + dp[i-1][j-1] # if the same char happened take value from diagonal
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# recover the answer
subsequence = []
i = N
j = M
while i >= 1 and j >= 1:
    max_value = max(dp[i - 1][j], dp[i][j - 1])
    if dp[i][j] == max_value + 1:  # it means that the i-1 in f_s and j-1 in s_s are the same, thus part of subsequence
        subsequence.append(f_s[i-1])
        i -= 1
        j -= 1
    elif dp[i][j-1] == max_value:  #choose the direction to go in dp (reverse algorithm)
        j -= 1
    else:
        i -= 1

print(*subsequence[::-1])

'''
Performance: P 3.11.2 (789 ms, 16.00 Mb); P 3.9 PyPy 7.3.11 (245 ms, 33.41 Mb)
Complexity: O(N*M)
Auxiliary Space: O(N*M)
Test cases:
1
1
1
1
ans: 1
1
1
1
2
ans: 
3
1 2 3
3 
3 2 1
ans: 1 or 2 or 3
3
1 2 3
3 
2 3 1
ans: 2 3
11
1 5 4 2 3 2 2 4 5 6 5
10
1 4 2 3 2 2 4 5 6 5
ans: 1 4 2 3 2 2 4 5 6 5
'''

