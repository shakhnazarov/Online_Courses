from collections import Counter

# initialize the input (note we dont know the exact number of inputs) (ctrl+D to cancel input in console)
# could use open('input.txt').read() here
raw_str = ""
while True:
    try:
        temp = input()
        raw_str += temp
    except:
        break

# delete whitespace from the input string
raw_str = "".join(raw_str.split())

# count all characters (dictionary[str] = int)
count_dict = Counter(raw_str)

'''
count_dict = {}
for char in raw_str:
    count_dict[char] = 1 + count_dict.get(char, 0)
'''

# sort the dictionary inplace(?)
count_dict = dict(sorted(count_dict.items()))

# find max num of occurrences
max_occurrences = 0
for val in count_dict.values():
    max_occurrences = max(max_occurrences, val)

# print out the #
for i in range(max_occurrences):
    print_str = ""
    for val in count_dict.values():
        if val + i >= max_occurrences:
            print_str += "#"
        else:
            print_str += " "
    print(print_str)

# print out the keys of dict
print_str = ""
for key in count_dict.keys():
    print_str += key
print(print_str)
