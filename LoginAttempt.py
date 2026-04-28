flag = 0
for i in range(3):
    password = input("Enter your Password:")

    if password == "333":
        print("Lgin Successful")
        flag = 1
        break
    else:
        print("Wrong Attempt")

if not flag:
    print("Account Locked!!!")
