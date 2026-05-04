#m elements constant
lst = eval(input("Enter a list: "))
k = int(input("Enter value of k: "))
m = int(input("Enter value of m (fixed elements): "))

n = len(lst)

if m < n:
    k = k % (n - m)
    for i in range(k):
        item = lst.pop(m)   
        lst.append(item)    
print(lst)