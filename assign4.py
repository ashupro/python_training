import random

class Person:
    def __init__(self,name,age,sex,grade):
        self.name=name
        self.age=age
        self.sex=sex
        self.grade=grade

    def display(self):
        print('i am {},{} years old {},i got {} percentage'.format(self.name, self.age, self.sex, self.grade))

arr=[]
sex=["male","female"]

def create25obj():
    for i in range(1,26):
        name = 'a'+str(i)
        per=random.random()*100
        obj = Person(name, i, random.choice(sex),round(per))
        arr.append(obj)

def display25obj():
    for ele in arr:
        ele.display()

create25obj()
display25obj()
