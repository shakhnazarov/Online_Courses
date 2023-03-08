# read input
M = int(input())
N = int(input())

# create set of tuples (start, end) of indices
systems = set()

# intersect the new system with the old
for i in range(N):
    beg, end = map(int, input().split())
    set_for_delete = set()  # cannot delete from set while iterating, thus, delete in one batch after loop
    for indices in systems:
        # check whether the system is intersecting with any existing
        if (beg <= indices[0] <= end) or (beg <= indices[1] <= end)\
                or indices[0] <= beg <= indices[1]:  # cover 2-3,7 cases or 3,5,7 cases or 4th case
            set_for_delete.add((indices[0], indices[1]))
        '''
        Note, overall seven cases are possible (_ - empty, X - old, O - new):
        ____XXXX____    ____XXXX____    ____XXXX____    ____XXXX____    ____XXXX____    ____XXXX____    ____XXXX____
        _00_________    ___000______    ____0  000____    _____00_____    ______000___    _________00_    ___000000___
        no overwrite    overwrite       overwrite       overwrite       overwrite       no overwrite    overwrite
        '''
    systems = systems.difference(set_for_delete)
    systems.add((beg, end))  # add later due to 3rd case above

# print out the number of remaining systems
print(len(systems))


# we can intersect lines by a <= d and c<=b for:
# a ------ b (a<=b)
#    c ------ d (c<=d

# Can solve O(NlogN) by sorting the systems and using binary_search  and balanced biniary search tree
'''
Complexity: O(N**2)
Auxiliary Space: O(N)
Test cases:
12
10
5 8
2 3
4 6
5 8
5 8
6 7
5 8
7 9
5 8
10 11
ans: 3
3
0
ans: 0
3
3
1 1
2 2
3 3
ans: 3
10
3
1 3
4 7
3 4
ans: 1
10
4
1 3
4 5
7 8
4 6
ans: 3'''

