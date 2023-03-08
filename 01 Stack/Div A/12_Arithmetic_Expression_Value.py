# read input
equation = input()
elements = list(equation.split())
DIGITS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
wrong = False

# check whether whitespace exists between numbers (if only a number is given in equation skip the check)
for i in range(len(elements)):
    if len(elements) != 1 and (elements[i][0] in DIGITS) and (elements[i-1][-1] in DIGITS):
        wrong = True
        break

# kind of cheating but still, use built-in function to evaluate string equation
try:
    ans = eval(''.join(elements))
except:
    wrong = True

# print out the answer
if not wrong:
    print(ans)  # ans exists only if wrong is False
else:
    print("WRONG")

'''
Time complexity: O(N)
Auxiliary space: O(N)
Test cases:
1+(2*2 - 3)
ans: 2
1+a+1
ans: WRONG
1 1 + 2
ans: WRONG
1
ans: 1
'''
