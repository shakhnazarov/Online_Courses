"""
As only one element is damaged we know that at max one tag might be incorrect
"""

def solution(xml):
    # check corner cases
    if xml[0] != '<':
        return '<' + xml[1:]
    if xml[-1] != '>':
        return xml[:len(xml)-1] + '>'

    tags_stack = []  # [tag, start index (from bracket)]
    i = 0
    while i != len(XML):
        if XML[i] == '<' and XML[i + 1] == '/':  # cannot be the case when < is last element
            i = i + 2
            temp_tag = ''
            while i != len(XML) and XML[i] != '>':
                temp_tag += XML[i]
                i += 1
            if tags_stack[-1] == temp_tag:
                tags_stack.pop()
            else:
                return "error"
        elif XML[i] == '<':
            i = i + 1
            temp_tag = ''
            while i != len(XML) and XML[i] != '>':
                temp_tag += XML[i]
                i += 1
            tags_stack.append(temp_tag)
        i += 1  # in correct XML for this row xml[i] == ">"


# read input
XML = input()

print(solution(XML))

# если <asdasz<ыфв>, то сразу знаешь где ошибка
<