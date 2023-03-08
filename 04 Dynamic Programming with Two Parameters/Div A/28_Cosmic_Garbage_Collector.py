"""
Use DP for each letter
Dynamics: for each letter we keep number of meters needed to execute the command
Step: step meter and iterate over letter's commands so that for each command we know what meters are needed
"""

# read input
letters = ['N', 'S', 'W', 'E', 'U', 'D']
commands = {}
for letter in letters:
    commands[letter] = input()
command_initial, num =  input().split()
num = int(num)

# set up the base (1 meter for letter 1 command), 0 added for consistency in indexing
dp = {}
for letter in letters:
    dp[letter] = [0, 1]

# note, that we keep (num+1)*6 in dp but could have num*6 + 1
for i in range(1, num+1):
    for letter in letters:
        temp = 1  # first we do a step in the direction
        for command in commands[letter]:
            temp += dp[command][i]  # for i+1 do each command inside a letter i times (but we know meters so take dp[i])
        dp[letter].append(temp)

print(dp[command_initial][num])

'''
Complexity: O(a*k*num) where a is number of letters (6), k is number of letters in the command and num is N
Auxiliary space: O(a*num)
Test cases:






S 10
ans: 1
N
NUSDDUSE
UEWWD

U
WED
S 3
ans: 34
'''