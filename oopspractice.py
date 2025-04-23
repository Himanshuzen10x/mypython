class person:
    def __init__ (self,name,age):
        self.name= name
        self.age= name
        
class employee(person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary= salary

    def display(self):
        print(f'Name: {self.name}')
        print(f'age: {self.age}')
        print(f'salary: {self.salary}')
        
employee1 = employee("himanshu", 21 , 50000)
employee1.display()