balance = int(input("Enter balance:"))
withdraw = int(input("Enter Amount withdraw:"))

if withdraw > (balance - 1000):
    print("transactiion failed: Minimum balance Voilation")
