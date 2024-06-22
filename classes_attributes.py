#oops
#create Classes
# Why class, how to make a class
# class vs instace
# functions inside a class
# Inheritance (parent class vs child classes)
# encapsulation (private/public methods)
# properties (getter/setter)
#Four principles of oops
# 1) Inheritance
# 2) polymorphism
# 3)Encapsulation
# 4)Abstraction

#create a class
lst_se1 = ["software engineer", "pranav", 23, "junior", "30000" ]
lst_se2 = ["software engineer", "harsha", 25, "senior", "50000"]
# designer_1 = ["designer", "harsha", 25, "senior", "50000"]



class SofwareEngineer:
    #class attribute
    sits_on = "always sits in chair"
    def __init__(self, name, age, level, salary):
        #Instance attributes belong to only object that we create out of mould
        #
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary



se_obj1 = SofwareEngineer("pranav", 23, "junior", "30000")
se_obj2 = SofwareEngineer("harsha", 25, "senior", "50000")
print(f" software engineer named {se_obj1.name}, with {se_obj1.age}  age"
      f" and position  {se_obj1.level}, gets {se_obj1.salary} salary")

print(se_obj2.name, se_obj2.age, se_obj2.level, se_obj2.salary)

print(f"se1 sits_on = {se_obj1.sits_on}")
print(f"se2 sits_on = {se_obj2.sits_on}")
print(f"sits_on = {SofwareEngineer.sits_on}")

print(f"name = {se_obj1.name}")
# print(f"name = {SofwareEngineer.name}")

#recap
# 1) how to create a classmethod
# 2) how to create instances
# 3) difference between class and instance
# 4)instance attributes are defined in  init function
# 5)class attributes
# 6) difference between class and instance attribute



