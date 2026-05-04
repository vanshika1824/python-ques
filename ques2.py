#rotate k times anti clock-wise
lst = eval(input("Enter a list:"))
k = int(input("Enter value of k:"))

for i in range(k):
    item = lst.pop()
    lst.insert(0,item)

print(lst)