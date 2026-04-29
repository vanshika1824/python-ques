#call of value:
def update(v):
    v="hi"
    print(v)

v="hello"
update(v)
print(v)

#call by Reference:
def update(lst):
    lst[0]=21

lst=[10,20,30,40,50]
update(lst)
print(lst)