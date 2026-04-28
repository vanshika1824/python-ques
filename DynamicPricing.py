base = int(input("Base Price:"))
demand = input("Demad(high/low):")
weekend = input("weekend(yes/no):")

if demand == "high" and weekend =="yes":
    base = base * 1.3
elif demand == "high":
    base = base * 1.2
elif weekend == "yes":
    base = base * 1.1

print("Final Price:",base)