#polyorphism - many shapes
#way to use a class like a paret class
#way to use  a class exactly like a parentclasss but the child will keep
# the  methods as they are

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

employee_lst = [SoftwareEngineer("pranav", 25, "20000", "junior"),
                Designer("sai", "34", "30000"),
                SoftwareEngineer("krishnaw", 52, "80000", "senior")]

for employee in employee_lst:
    employee.work()


# emp1 = Employee("sudhakar", 28, "50000" )
# emp1.work()
#
# se1_obj = SoftwareEngineer("pranav", 25, "20000", "junior")
# #print(se1_obj.name, se1_obj.age)
# se1_obj.work()
#
#
#
# d_obj = Designer("sai", "34", "30000")
# #print(d_obj.name, d_obj.age)
# d_obj.work()


#Recap
# 1) inheritance child, parent class
# 2) inherit, extend, override ( attributes and methods)
# 3) Super
# 4) polymorphism