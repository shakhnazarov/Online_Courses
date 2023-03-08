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
# conventional solution is too slow
    for j in range(x1-1, x2):  # coordinates start from 1 but indices from 0
        for k in range(y1-1, y2):
            ans += matrix[j][k]
'''