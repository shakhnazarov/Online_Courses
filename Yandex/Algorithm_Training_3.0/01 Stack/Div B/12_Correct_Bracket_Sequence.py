"""
Use stack and compare the input to top element of the stack
"""
# read input
s = input()

# implement stack data structure to solve the problem
stack = []
correct_sequence = True  # decide what to print depending on correctness
for c in s:
    match c:
        case "(":
            stack.append("(")
        case "{":
            stack.append("{")
        case "[":
            stack.append("[")
        case "]":
            try:  # might be neater in a function, without heavy repetition
                if stack.pop() != "[":
                    correct_sequence = False
                    break
            except IndexError:
                correct_sequence = False
                break
        case "}":
            try:
                if stack.pop() != "{":
                    correct_sequence = False
                    break
            except IndexError:
                correct_sequence = False
                break
        case ")":
            try:
                if stack.pop() != "(":
                    correct_sequence = False
                    break
            except IndexError:
                correct_sequence = False
                break

# print out the answer
if correct_sequence and len(stack) == 0:  # if stack is empty at the end it is not correct sequence
    print("yes")
else:
    print("no")

'''
Performance: P 3.11.2 (59 ms, 4.41 Mb); P 3.9 PyPy 7.3.11 (Compilation Error)
Complexity: O(N)
Auxiliary Space: O(1)
Test cases:
(
ans: no
()[]
ans: yes
([)]
ans: no
'''