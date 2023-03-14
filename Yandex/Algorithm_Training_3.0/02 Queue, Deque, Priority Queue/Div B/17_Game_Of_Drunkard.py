"""
Follow the rules of the game with pair of stacks
"""
# read input
first_cards = list(map(int, input().split()))
second_cards = list(map(int, input().split()))

# dummy for whether the game has ended within specified number of acts
botva = True

# Use queue to solve
for i in range(10**6):
    try:
        first = first_cards.pop(0)
    except IndexError:  # catch error if queue is empty
        print(f"second {i}")
        botva = False  # as we have finished game with the winner - no botva
        break
    try:
        second = second_cards.pop(0)
    except IndexError:
        print(f"first {i}")
        botva = False
        break
    if first == 0 and second == 9:  # smallest card beats the highest
        first_cards.append(first)
        first_cards.append(second)
    elif first == 9 and second == 0:
        second_cards.append(first)
        second_cards.append(second)
    elif first > second:  # otherwise higher card beats lower
        first_cards.append(first)
        first_cards.append(second)
    else:  # cannot be first==second
        second_cards.append(first)
        second_cards.append(second)

if botva:
    print("botva")

'''
Performance: P 3.11.2 (43 ms, 4.41 Mb); P 3.9 PyPy 7.3.11 (172 ms, 28.09 Mb)
Time: O(N)
Auxiliary Space: O(1)
Test Cases:
0 1
1 0
ans: botva
1 3 5 7 9
2 4 6 8 0
ans: second 5
2 4 6 8 0
1 3 5 7 9
ans: first 5
1 7 3 9 4
5 8 0 2 6
ans: second 23
'''
