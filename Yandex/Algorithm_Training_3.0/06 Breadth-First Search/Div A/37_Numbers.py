"""
Use state graph
"""

def bfs():
    for length in range(len(paths)):
        for vertex in paths[length]:
            # add to the first digit 1
            if vertex//1000 != 9 and nums[vertex+1000] == -1:
                nums[vertex+1000] = length + 1
                paths[length+1].append(vertex+1000)
            # extract from the last digit 1
            if vertex%10 != 1 and nums[vertex-1] == -1:
                nums[vertex-1] = length + 1
                paths[length+1].append(vertex-1)
            # cyclic shift to the left
            if nums[(vertex%1000)*10 + vertex//1000] == -1:
                nums[(vertex%1000)*10 + vertex//1000] = length + 1
                paths[length+1].append((vertex%1000)*10 + vertex//1000)
            # cyclic shift to the right
            if nums[vertex//10 + (vertex%10)*1000] == -1:
                nums[vertex//10 + (vertex%10)*1000] = length + 1
                paths[length+1].append(vertex//10 + (vertex%10)*1000)




# read input
f_num = int(input())
s_num = int(input())

# construct nums as shortest distance from f_num
nums = [-1 for i in range(10001)]
nums[f_num] = 0

# find all length to all states from f_num (~6000 numbers)
paths = [[] for _ in range(9*4+1)]
paths[0].append(f_num)
bfs()

# recover the answer
ans = [s_num]
l = nums[s_num]
curr_num = s_num
for l in range(nums[s_num]-1, -1, -1):
    if curr_num - 1000 in paths[l]:  # reverse operation (thus -1000 not +1000)
        curr_num = curr_num - 1000
    elif curr_num + 1 in paths[l]:
        curr_num = curr_num + 1
    elif (curr_num % 1000) * 10 + curr_num//1000 in paths[l]:
        curr_num = (curr_num % 1000) * 10 + curr_num//1000
    else:  # curr_num // 10 + curr_num[3] * 1000 in paths[l]:
        curr_num = curr_num // 10 + (curr_num%10) * 1000
    ans.append(curr_num)

# print out the answer in reverse
print(*ans[::-1])

'''
Time complexity: O(a)  # a - len of the number
Auxiliary Space: O(b)  # b - max possible number
1111
9999
ans: 1111 2111 3111 4111 5111 6111 7111 8111 9111 1911 2911 3911 4911 5911 6911 7911 8911 9911 1991 2991 3991 4991 5991 6991 7991 8991 9991 1999 2999 3999 4999 5999 6999 7999 8999 9999
1234
4321
ans: 1234 1233 1232 2321 3321 4321
'''
