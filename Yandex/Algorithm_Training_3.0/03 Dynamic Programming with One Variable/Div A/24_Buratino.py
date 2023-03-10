"""
Use forward DP
Dynamics: max number of nails Papa Carlo can hammer for ith second since the beginning of the shift (note, seperate
dynamics for fist and second part of the shift)
Step: compare whether doing nothing in the last period is better than the current case and update future values given
now we start to hammer a nail
"""
# read input
N = int(input())

# set up the constants
START_SHIFT = 9
END_FIRST_PART = 13
START_SECOND_PART = 14
END_SHIFT = 18
FIRST = 3600*(END_FIRST_PART-START_SHIFT)
FIRST_LUNCH = 3600*(START_SECOND_PART-START_SHIFT)
SECOND = 3600*(END_SHIFT-START_SECOND_PART)

# we want for O(1) get how many seconds will Papa Carlo spend hammering nail if watch a show in ith time
shows = [0 for _ in range(FIRST_LUNCH + SECOND+1)]
old_start, old_t_work = input().split()  # always start at 9:00:00
old_start = 0
for i in range(1, N):  # already unpack first string
    start, t_work = input().split()
    hh, mm, ss = map(int, start.split(':'))
    start = 3600*(hh-START_SHIFT) + 60*mm + ss
    for j in range(old_start, start):
        shows[j] = int(old_t_work)
    old_start = start
    old_t_work = t_work
for j in range(old_start, len(shows)):
    shows[j] = int(old_t_work)

# compute dynamics for each i for first part of work
dp_f = [0 for _ in range(FIRST+2)]  #dp[i] is max number of nails when i+1th second **begins**
for i in range(1, FIRST+2):
    dp_f[i] = max(dp_f[i], dp_f[i-1])
    if shows[i-1] + i <= FIRST+1:
        dp_f[i+shows[i-1]] = max(dp_f[i] + 1, dp_f[i+shows[i-1]])  # -1 for shows as they get time for beg of ith sec

# compute dynamics for second part of the shift
dp_s = [0 for _ in range(SECOND+2)]
for i in range(1, SECOND+2):
    dp_s[i] = max(dp_s[i], dp_s[i - 1])
    if shows[FIRST_LUNCH + i - 1] + i <= SECOND+1:
        dp_s[i + shows[FIRST_LUNCH + i - 1]] = max(dp_s[i] + 1, dp_s[i + shows[FIRST_LUNCH + i - 1]])

print(dp_f[-1] + dp_s[-1])

'''
Complexity: O(N)
Auxiliary Space: O(N)
Test Cases:
2
09:00:00 3600
14:00:00 3600
ans: 8
4
09:00:00 1800
12:59:31 10
13:45:23 1800
15:00:00 3600
ans: 14
1
09:00:00 32400
ans: 0
2
09:00:00 14400
14:00:00 14400
ans: 2
'''