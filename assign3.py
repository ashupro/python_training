import random

class Person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def display(self):
        print('i am {}, {} year old {}'.format(self.name, self.age, self.sex))
arr=[]
arr1=[]
arr2=[]
arr3=[]
sex=["male","female", "others"]

def create25obj():
    for i in range(1, 26):
        name = 'a'+ str(i)
        obj = Person(name, i, random.choice(sex))
        arr.append(obj)

def segregate():
    for ele in arr:
        if(ele.sex=='male'):
            arr1.append(ele)
        elif(ele.sex=='female'):
            arr2.append(ele)
        else:
            arr3.append(ele)

def display25obj():
    for ele in arr1:
        ele.display()
    for ele in arr2:
        ele.display()
    for ele in arr3:
        ele.display()

create25obj()
segregate()
display25obj()

print("number of males is ",len(arr1))
print("number of femalesis ",len(arr2))
print("number of others is ",len(arr3))
