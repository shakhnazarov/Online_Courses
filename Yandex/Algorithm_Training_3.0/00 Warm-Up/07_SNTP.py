from math import ceil

# read input
A_hh, A_mm, A_ss = map(int, input().split(":"))
B_hh, B_mm, B_ss = map(int, input().split(":"))
C_hh, C_mm, C_ss = map(int, input().split(":"))

# get the difference of individual terms
diff_hh = C_hh - A_hh
diff_mm = C_mm - A_mm
diff_ss = C_ss - A_ss

# we will convert overall diff to total seconds
seconds = 0

# note that diff can be negative thus next day is considered
if diff_hh >= 0:
    seconds += diff_hh * 3600
else:
    seconds += (diff_hh + 24) * 3600

# if diff_mm < 0 then we added excessive hour in previous calculations
if diff_mm >= 0:
    seconds += diff_mm * 60
else:
    seconds += (diff_mm + 60) * 60 - 3600

# if diff_s < 0 then we added excessive minute in previous calculations
if diff_ss >= 0:
    seconds += diff_ss
else:
    seconds += (diff_ss + 60) - 60

# calculated total deliver time but need one only (note that we need int and round produces float)
seconds = ceil(seconds / 2)

# convert what we need to add for B time
ans_hh = seconds // 3600
seconds -= ans_hh * 3600
ans_mm = seconds // 60
ans_ss = seconds % 60

# term by term add ans to B, check whether overflow limit of time measurement
ans_ss += B_ss
if ans_ss >= 60:
    ans_ss -= 60
    ans_mm += 1

ans_mm += B_mm
if ans_mm >= 60:
    ans_mm -= 60
    ans_hh += 1

ans_hh = (ans_hh + B_hh) % 24

# convert to time format
if ans_hh < 10:
    ans_hh = "0" + str(ans_hh)
if ans_mm < 10:
    ans_mm = "0" + str(ans_mm)
if ans_ss < 10:
    ans_ss = "0" + str(ans_ss)

# print answer
print(f"{ans_hh}:{ans_mm}:{ans_ss}")
