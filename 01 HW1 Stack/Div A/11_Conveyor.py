# implement binary search
def binary_search(arr, value):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == value:
            while mid != 0 and arr[mid-1] == arr[mid]:  # when several identical values exist need the first one
                mid -= 1
            return mid
        elif arr[mid] > value:
            right = mid - 1
        else:
            left = mid + 1

    return "error"

# !!! FIXME во 2 тесте ошибка
# read initial input
N = int(input())

for i in range(N):
    # read conveyer items' priorities
    K, priorities = input().split(maxsplit=1)
    K = int(K)
    priorities = list(map(float, priorities.split()))
    priorities_sorted = sorted(priorities)
    priorities_sorted.insert(0, priorities_sorted[0] - 1)  # cannot just add 0, negative values possible (?)
    warehouse = []
    A = [priorities_sorted[0]]

    for j in range(K):
        warehouse.append(priorities[j])  # action "A -> B" is the same as "A -> warehouse -> B"
        # check whether last element in A is the next item in terms of priority
        while len(warehouse) != 0 and\
                (A[-1] == priorities_sorted[binary_search(priorities_sorted, warehouse[-1]) - 1]
                or A[-1] == warehouse[-1]):  # check whether the same priority
            A.append(warehouse.pop())

    # if stack is not empty then we cannot arrange from A to B in terms of priority
    if len(warehouse) == 0:
        print(1)
    else:
        print(0)


'''
Complexity: O(N*K*logK)  # sorting is KlogK and K times binary search also KlogK
Auxiliary space: O(K)
Test cases:
2
2 2.9 2.1
3 5.6 9.0 2.0
ans: 1 0
1
1 1
ans: 1
1
5 3000000000.1 3000000000.1 3000000000.1 3000000000.1 3000000000.1
ans: 1
'''








