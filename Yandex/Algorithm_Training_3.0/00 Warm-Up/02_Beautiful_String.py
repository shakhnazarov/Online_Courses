"""
Use two pointers to widen window as long as chars within window can be changed for the same ones
# you can solve it by binary_search and prefix sums
"""

# read input
k = int(input())
s = input()

# use two pointers technique, first check whether window is bigger than degree of freedom
if k >= len(s) - 1:
    print(len(s))
else:
    # compute initial dictionary of values for k positions
    chars_freq = {}
    for i in range(2): # initialize dictionary
        chars_freq[s[i]] = chars_freq.get(s[i], 0) + 1

    # compute whether chars are identical
    max_count = max(chars_freq.values())

    # initialize left and right indices
    l = 0
    r = 1

    while r < len(s)-1:  # each iteration we increase r by 1, len(s) - 1 as use r+1 inside
        if chars_freq.get(s[r + 1], 0) == max_count:  # could stumble upon unknown char
            max_count += 1
        elif r-l+1 - max_count >= k: # we have spare space of k for changing chars
            chars_freq[s[l]] -= 1  # go out from left side thus, char is no longer in the window
            l += 1
        chars_freq[s[r + 1]] = 1 + chars_freq.get(s[r + 1], 0)  # widen window to the right, increase char occurrence
        r += 1

    # max and terminal size of the window
    print(r - l + 1)


'''
Performance: P 3.11.2 (303 ms, 4.40 Mb); P 3.9 PyPy 7.3.11 (220 ms, 28.09 Mb)
Complexity: O(N)  # N = length of string S
Auxiliary Space Complexity: O(b)  # b ~ 26 size of alphabet
Test Cases:
2
abcaz
ans: 4
400
gcasnpanxtiqghxayrxpvyagmtzapagsqdrsojldoqnugrphltmbjxvklngocdgjcxitufotwuvejpizwmtulmwygurtoizcluuzxuvdqiiffmrwfhkpylmwguotjmgzhvobpaksssgpaocqisuvghbvylrfdaportmfmtydjcwoqqxpbnmkaiaewnwdwvqavgvzvmyqmslhaavtsuohpayxhqgyfsorriqkaizgiryruysygrpmhkprpkyrsolqfclojcltwwjfmnyffewumwbwcfvhlhhhbzdfztiucqbtowrfkwlydzuekwrjyqncofjauzgjhbxqwbcayatdhzkmdpzitzxycopstcqbshvspkfvberfguqeezgxhyrngbkunsngcumurssigqlrphnrfxprmsgivrfvgxygakvkgzubwrssprzdfpirsjuyvxbtygbnpbxhepnxiejjwwtejvpbnibpjngjyfiriciejdaercjnjaqigsyjlybmqrtpxwrcfpmshgdhevqfwapvzjfygtnohydurikqpdekeogokjcneeejgsvkbdahjtcwfiyplbibznzjtvtrdvrlscjfcuzpbvxgewwzppswariagkadfjsrcmhpbnmuqucocsydquoutnarkkttjqywlwqpokwkoaiduvcjmgxqvszwhhwcjfnkoomhjxuviclndzuirqkfjoukkaanrhhrkbarrecfvhvddecejbccffnjncmvnsryredcqzgluligofbgibxbuaeiybbydczzovczsiiessvdgdlunwwzaoapiuwxjyjloxovzgkmpnjvjqejmpikontkiovaeiyfjhrzplzaqjjvyqrkkntzkpngexbiemqlnnhwtjmoeezybqwhomkulryhgzbzixlkrtnnjxxyghdbkcacfbsuafrwafvahqevzeurddnvzzobzzlhgkuurjawjejuurjywnbvflttfasweaxm
ans: 432
'''