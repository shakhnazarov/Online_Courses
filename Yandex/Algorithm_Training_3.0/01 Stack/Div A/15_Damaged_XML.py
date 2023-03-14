"""
As limitations are of N <= 1000 then we can check each possible variation of the string and find the correct one
"""
# read input
XML = input()

alphabet = ['<', '>', '/']  # list is easier for debugging compared to set
for i in range(26):  # 26 letters in English alphabet
    alphabet.append(chr(ord('a') + i))  # ord gets ASCII value of a character, chr maps ASCII to char

# check corner cases
is_correct = False
XML_changed = XML
if XML[0] != '<':
    XML_changed = '<' + XML[1:]
    is_correct = True
if XML[-1] != '>':
    XML_changed = XML[:len(XML)-1] + '>'
    is_correct = True

for ch in alphabet:
    if is_correct:
        break
    for i in range(1, len(XML)-1):  # already checked corner cases above
        if is_correct:
            break
        XML_changed = XML
        XML_changed = XML_changed[:i] + ch + XML_changed[i+1:]  # as strs are immutable use slices to assign new char
        j = 0
        tags_stack = []
        while j < len(XML_changed):
            if XML_changed[j] == '<' and XML_changed[j + 1] == '/':  # cannot be the case when < is last element
                j += 2  # skip < and / chars
                temp_tag = ''
                while j != len(XML_changed) and XML_changed[j] != '>':
                    temp_tag += XML_changed[j]
                    j += 1
                if len(tags_stack) != 0 and tags_stack[-1] == temp_tag:
                    tags_stack.pop()
                else:
                    break
            elif XML_changed[j] == '<' and XML_changed[j+1] not in {'<','>'}:
                j += 1
                temp_tag = ''
                while j != len(XML_changed) and XML_changed[j] != '>':
                    temp_tag += XML_changed[j]
                    j += 1
                tags_stack.append(temp_tag)
                # could be error in tag, and we could replicate the same error in opposite tag
                if '<' in temp_tag or '>' in temp_tag or '/' in temp_tag:
                    break
            else:
                break
            j += 1  # in correct XML for this row XML_changed[j] == ">"
            if j == len(XML_changed) and len(tags_stack) == 0:  # got to the end of the loop
                is_correct = True

print(XML_changed, end='')

'''
Performance: P 3.11.2 (291 ms, 23.54 Mb); P 3.9 PyPy 7.3.11 (280 ms, 45.69 Mb)
Complexity: O(a*N^2)  # a is size of alphabet (29)
Auxiliary Space: O(N)
Test cases:
<a></b>
ans: <a></a>
<a><aa>
ans: <a></a>
<a><>a>
ans: <a></a>
<a/</a>
ans: <a></a>
'''