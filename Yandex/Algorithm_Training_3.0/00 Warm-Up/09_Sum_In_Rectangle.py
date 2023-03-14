"""
Use prefix sum where pref[i][j] is the sum of values for matrix from left top corner to i, j
"""

# read input matrix
N, M, K = map(int, input().split())
matrix = [[] for x in range(N)]  # NxM matrix
for i in range(N):
    matrix[i] = list(map(int, input().split()))

# compute prefix sums of matrix (initialize by first in row elements to retrieve by index)
matrix_prefix = [[0] for x in range(N+1)] # it will be (N+1)x(M+1) matrix (first row/column of zeros)

# compute row prefix sums of matrix
matrix_prefix[0] = [0]*(M+1)  # first row of zeros
for i in range(N):
    for j in range(M):
        matrix_prefix[i+1].append(matrix[i][j] + matrix_prefix[i+1][-1]) # start from 2nd row as if from 1st

# compute prefix sums of prefix matrix by column
for i in range(M):  # start from second column by i+1
    for j in range(N):  # start from second row by j+1
        matrix_prefix[j+1][i+1] += matrix_prefix[j][i+1]


# combine input and solution
for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    # as we know cumulative function, just take the difference to find value of square interval
    ans = matrix_prefix[x2][y2] - matrix_prefix[x2][y1-1] - matrix_prefix[x1-1][y2] + matrix_prefix[x1-1][y1-1]

    # print out the answer
    print(ans)

'''
Performance: P 3.11.2 (2028 ms, 76.86 Mb); P 3.9 PyPy 7.3.11 (859 ms, 44.43 Mb)
Complexity: O(N**2)
Auxiliary Space: O(N**2)
Test cases:
3 3 2
1 2 3
4 5 6
7 8 9
2 2 3 3
1 1 2 3
ans: 28 21
'''