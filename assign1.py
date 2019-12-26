class Person:
    def __init__(self, name, age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def display(self):
        print('i am {1}, {0} year old {2}' .format(self.name,self.age,self.sex))
        print ("hello")

obj1 = Person('ashu', 29, 'female')
obj1.display()
obj2 = Person('arun', 29, 'male')
obj2.display()

