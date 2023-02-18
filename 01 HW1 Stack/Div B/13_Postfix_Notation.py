# read input
list_input = input().split()

# use stack for Reverse Polish Notation
stack = []

for elem in list_input:
    match elem:
        case "+":
            stack.append(stack.pop() + stack.pop())
        case "-":
            stack.append((-1) * stack.pop() + stack.pop())  # 1st to last - 2nd to last
        case '*':
            stack.append(stack.pop() * stack.pop())
        case _:
            stack.append(int(elem))

# print out the result (should always be only one element in stack)
print(stack[0])
