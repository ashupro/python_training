import random
import sys

class Person:
        def __init__(self, name, age, sex):
            self.name=name
            self.age=age
            self.sex=sex

        def display(self):
            str = 'i am {}, {} year old {}'.format(self.name, self.age, self.sex)
            print(str)


arr=[]
def create_25_obj():
    sex=['male','female']
    for i in range(1,26):
        name = 'a'+ str(i)
        obj = Person(name, i, random.choice(sex))
        arr.append(obj)

def display_all_obj_in_array():
    for i in arr:
        i.display()

create_25_obj()
display_all_obj_in_array()

x = int(sys.argv[1])
arr[x-1].display()