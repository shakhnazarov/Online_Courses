# read input
N = int(input())

for i in range(N):
    # read conveyer items' priorities
    K, priorities = input().split(maxsplit=1)
    K = int(K)
    priorities = list(map(float, priorities.split()))
    priorities_sorted = sorted(priorities)
    priorities_sorted.insert(0, priorities_sorted[0] - 1)  # cannot just add 0, negative values possible (?)
    warehouse = []
    k = 0  # keep the relative number of the last element in B line

    for j in range(K):
        warehouse.append(priorities[j])  # action "A -> B" is the same as "A -> warehouse -> B"
        # check whether last element in A is the next item in terms of priority
        while len(warehouse) != 0 and priorities_sorted[k+1]==warehouse[-1]:
            warehouse.pop()
            k +=1

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




