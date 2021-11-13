time = str(input())


if time[-2:] == "AM":
    if time[:2] == "12":
        print("00" + time[2:-2])
    else:
        print(time[:-2])
else:
    if time[:2] == "12":
        print("12" + time[2:-2])
    else:
        temp = str(int(time[:2])+12)
        print(temp+time[2:-2])
# 12:00:00AM

"""
11:21:30PM  23:21:30
12:12:20AM   00:12:20
"""
