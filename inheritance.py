# inheritance is the process through which one class takes aon attributes
# and methods of the another class

#newly formed class is called the child class
#-> other one - parent class


#Inherit , extend , override

class Employee:
    def __init__(self, name , age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")

class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary )
        self.level = level

    # def debug(self):
    #     print(f"{self.name} is debugging")

    def work(self):
        print(f"{self.name} is coding")

class Designer(Employee):

    # def draw(self):
    #     print(f"{self.name} is drawing...")
    #
    def work(self):
        print(f"{self.name} is designing")

emp1 = Employee("sudhakar", 28, "50000" )
emp1.work()

se1_obj = SoftwareEngineer("pranav", 25, "20000", "junior")
#print(se1_obj.name, se1_obj.age)
se1_obj.work()



d_obj = Designer("sai", "34", "30000")
#print(d_obj.name, d_obj.age)
d_obj.work()