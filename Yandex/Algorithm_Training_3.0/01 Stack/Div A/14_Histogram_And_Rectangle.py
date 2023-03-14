"""
Rectangle is the biggest if it cannot grow to the left, right, up. Thus, find for each bin (fixing the height)
the nearest neighbors which are lower than the height, hence, bounding the rectangle. Then just choose the max one
"""
# read input
N, hist = input().split(maxsplit=1)
N = int(N)
hist = [[int(x), -1, N] for x in hist.split()]  # [height, left lower neighbor, right lower neighbor]

# for each bin find the nearest lower neighbor from the right
stack_neighbor = [[hist[0][0], 0]]  # [value, index]
for i in range(1, N):
    while len(stack_neighbor) != 0 and hist[i][0] < stack_neighbor[-1][0]:
        hist[stack_neighbor.pop()[1]][2] = i  # add the index of the nearest right lower neighbor
    stack_neighbor.append([hist[i][0], i])

# for each bin find the nearest lower neighbor from the left
stack_neighbor = [[hist[N-1][0], N-1]]  # [value, index]
for i in range(N-2, -1, -1):
    while len(stack_neighbor) != 0 and hist[i][0] < stack_neighbor[-1][0]:
        hist[stack_neighbor.pop()[1]][1] = i  # add the index of the nearest left lower neighbor
    stack_neighbor.append([hist[i][0], i])

# find max rectangle for each bin and find overall max
max_rectangle = 0
for bin_hist in hist:
    max_bin = bin_hist[0] * (bin_hist[2] - bin_hist[1] - 1)
    if max_rectangle < max_bin:
         max_rectangle = max_bin

print(max_rectangle)

'''
Performance: P 3.11.2 (291 ms, 23.54 Mb); P 3.9 PyPy 7.3.11 (280 ms, 45.69 Mb)
Complexity: O(N)
Auxiliary Space: O(N)
Test Cases:
5 5 5 5 5 5
ans: 25
1 10
ans: 10
6 6 5 4 3 2 1
ans: 12
6 1 2 3 4 5 6
ans: 12
7 2 1 4 5 1 3 3
ans: 8'''