# read input
equation = input()

# convert from infix to postfix notation
stack = []
postfix = []
operations = {'!':0, '&':1, '|':2, '^':2}  # the lower the operations[operation] the bigger is the priority
brackets = {'(', ')'}
for char in equation:
    if char in operations:
        # if first part is false second and third won't execute (will not get error in operations[stack[-1]])
        while len(stack) != 0 and stack[-1] != '(' and operations[char] >= operations[stack[-1]]:
            postfix.append(stack.pop())
        stack.append(char)
    elif char in brackets:
        if char == '(':
            stack.append(char)
        else:
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # remove opening bracket

    else:
        postfix.append(int(char))

# some operations might e still in stack
while len(stack) != 0:
    postfix.append(stack.pop())

# compute the value of equation
operands_stack = []
for elem in postfix:
    match elem:
        case '!':
            # assume it can be only in the beginning of expression or after the bracket
            operands_stack[-1] = 0 if operands_stack[-1] else 1
        case '&':
            # don't use arr.append(arr.pop() and arr.pop()) as for arr[-1]==0
            # Python will stop executing and won't delete 2 elements
            res_temp = operands_stack[-2] and operands_stack[-1]
            operands_stack.pop()
            operands_stack.pop()
            operands_stack.append(res_temp)
        case '|':
            res_temp = operands_stack[-2] or operands_stack[-1]
            operands_stack.pop()
            operands_stack.pop()
            operands_stack.append(res_temp)
        case '^':
            operands_stack.append(operands_stack.pop() ^ operands_stack.pop())
        case _:
            operands_stack.append(elem)

print(operands_stack[-1])

'''
Complexity: O(N)
Auxiliary Space: O(N)
Test cases:
1|(0&0^1)
ans: 1
!1
ans: 0
'''
