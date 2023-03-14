"""
Use binary search to find the needed sticker
"""
def binary_search(num):
    # check whether array is empty (len(diego_nums)==0):
    if N == 0:
        return 0
    # check whether num is greater than max as algorithm won't work properly
    if num > max_num:
        return N

    # define initial indices for binary search
    low = mid = 0
    high = N - 1

    while low <= high:
        mid = (low + high) // 2

        # if num is greater, ignore left half
        if num > diego_nums[mid]:
            low = mid + 1
        elif num < diego_nums[mid]:
            high = mid - 1
        else:
            return mid

    # if didn't find - use the left neighbor of num (note we cannot get num==diego_nums[mid] here
    if num > diego_nums[mid]:
        return mid + 1
    else:
        return mid


# read input Diego
N = int(input())
# N could be 0, then just read input
if N > 0:
    diego_nums = sorted(list(set(map(int, input().split()))))
    # calculate max number beforehand
    max_num = diego_nums[-1]
    # update N as duplicates have been erased
    N = len(diego_nums)
else:
    diego_nums = set()
    input()

# read input collectors
K = int(input())
# K could be 0, then just read input
if K > 0:
    collectors_nums = list(map(int, input().split()))
else:
    collectors_nums = []
    input()

# use binary search for each collector
for i in range(K):
    print(binary_search(collectors_nums[i]))

'''
Performance: P 3.11.2 (497 ms, 18.75 Mb); P 3.9 PyPy 7.3.11 (347 ms, 58.64 Mb)
Complexity: O(NlogN)
Auxiliary Space Complexity: O(1)
Test Cases:
1
5
2
4 6
ans: 0 1
4
3 3 2 2
4
3 3 4 2
ans: 1 1 2 0
'''
