"""
Use Dynamics on substrings
for:
10 3
2 4 7
~   0   2   4   7   10
0   0   0   4   11  20
2   0   0   0   5   13
4   0   0   0   0   6
7   0   0   0   0   0
10  0   0   0   0   0

"""
# read input
L, N = map(int, input().split())
cuts = [0]
cuts.extend(list(map(int, input().split())))
cuts.append(L)

# set up base case for dp
dp = [[0 for _ in range(len(cuts))] for __ in range(len(cuts))]

# go through diagonals
for diff in range(2, len(cuts)):  # for beams with num_cuts -1 and 0 ans is 0
    for l in range(len(cuts) - diff):
        r =  diff + l
        min_temp = float('inf')
        for i in range(l+1, r):  # check each partition (e.g. for beam 0 7 with needed cuts 2 and 4, check cut 2 and 4)
            min_temp = min(min_temp, dp[l][i] + dp[i][r])
        dp[l][r] = cuts[r] - cuts[l] + min_temp  # regardless of which point to cut always pay the length of the beam

print(dp[0][-1])

'''
Complexity: O(N^3)
Auxiliary Space: O(N^2)
Test Cases:
100 3
15 50 75
ans: 200
100 1
3
ans: 100
'''
