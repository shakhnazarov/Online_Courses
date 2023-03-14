"""
Iterate over the word and count mathy occurences (see pattern)
"1234"  "234"   "34"    "4"
"123"   "23"    "3"
"12"    "2"
"1"
"""
# read input
raw_str = input()

# create dictionary for counting chars
ans_dict = {}

n = len(raw_str)
for i, char in enumerate(raw_str):
    ans_dict[char] = ans_dict.get(char, 0) + (n-i)*(i+1)

# print result in sorted order
ans_dict = dict(sorted(ans_dict.items()))
for key, value in ans_dict.items():
    print(f"{key}: {value}")

'''
Performance: P 3.11.2 (75 ms, 4.41 Mb); P 3.9 PyPy 7.3.11 (359 ms, 28.09 Mb)
Complexity: O(N)  # N = length of the string
Auxiliary Space: O(b)  # b = size of alphabet
Test cases:
abacaba
ans: a: 44 b: 24 c: 16
'''