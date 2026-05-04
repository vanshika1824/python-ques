#2nd largest and 3rd smallest
lst = eval(input("Enter a list:"))

max,smax=lst[0],lst[0]
min,smin,tmin = lst[0],lst[0],lst[0]
for i in lst:
    if i>max:
        smax = max
        max = i

    else:
        if i>smax:
            smax = i

for i in lst:
    if i<min:
        tmin = smin
        smin = min
        min = i
    elif i<smin:
        tmin = smin
        smin = i
    elif i<tmin:
        tmin = i

print(smax,tmin)