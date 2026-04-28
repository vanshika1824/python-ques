avail = 0
seats = int(input("Seats required:"))
vip = input("Enter VIP Status(ys/no):")

if vip == "yes" or seats<avail:
    print("Tickect Confirmed")
else:
    print("Waiting...")