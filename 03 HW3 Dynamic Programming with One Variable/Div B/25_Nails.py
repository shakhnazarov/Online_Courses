# read input
N = int(input())
nails = list(map(int, input().split()))
nails.sort()
distance = nails[1] - nails[0] + nails[-1] - nails[-2]
if N==2:
    distance //= 2
i = 2
while i<N-2:
    if nails[i] - nails[i-1] <  nails[i+1] - nails[i]:
        distance += nails[i] - nails[i-1]
        i += 1
    else:
        distance += nails[i+1] - nails[i]
        i += 2



print(distance)

'''
Test cases:
6
1 2 3 4 5 6
ans: 3'''