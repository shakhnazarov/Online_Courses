# split a list by 0
def split(arr):
    res = []
    temp = []
    for elem in arr:
        if elem != 0:
            temp.append(elem)
        elif len(temp) != 0:
            res.append(temp)
            temp = []  # cannot use temp.clear() as appended value to res also clears
    if len(temp) != 0:  # if we added the last element to temp we go out from the cycle
        res.append(temp)
    return res


# read input
N = int(input())

letters = []
for i in range(N):
    letters.append(int(input()))

general_list = [letters]
ans = 0

# each time find min in a subset and create a zero element, divide by 0 and repeat
while len(general_list) != 0:
    for i, subset in enumerate(general_list):  # !!! Perhaps create too many copies
        min_temp = min(subset)
        ans += (len(subset) - 1) * min_temp  # can repeat min_temp consecutive sequences
        general_list[i] = [x - min_temp for x in subset]  # subtract a value from each element in the list
        for split_subset in split(general_list[i]):
            general_list.append(split_subset)
        del general_list[i]  # delete subset as divided by zero subsets already added

# print out the answer
print(ans)

'''
Test cases:
7
2
3
4
1
2
3
4
Ans: 12
'''
