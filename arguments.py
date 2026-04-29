#1. Positional Arguments
def profile(name,age):
    print("Name:",name)
    print("Age:",age)

profile("Aditya",21)
profile(21,"Aditya")

#2. Default Aruments:
def profile(name,age,alive="yes"):
    print("Name:",name)
    print("Age:",age)
    print("Alive:",alive)
    print(name,age,alive)

profile("Aditya",100,"no")

#3. Keyword Arguments:
def profile(name,age):
    print("Name:",name)
    print("Age:",age)

profile(age=21,name="Aditya")

#4. Multiple Arguments:
def add(*num):
    sum=0
    for i in num:
        sum+=i
    print(sum)

add(5,10,15)

#5. Multiple Keyword Arguments:(** kwargs)
def profile(**data):
    for i in data:
        print(data[i])

profile(name="vanshika",age=21,phone=134253673)