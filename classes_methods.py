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
designer_1 = ["designer", "harsha", 25, "senior", "50000"]

def can_code(lst):
    print(f"{lst[1]} can  code" )

# can_code(lst_se2)

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
    def code(self):
        print(f"{self.name}  is coding")

    def codes_in_language(self, language):
        """
        This function takes parameter language the SE codes and prints it

        :param language:
        :return:
        """
        print(f"{self.name} codes in {language}")
    def information(self):
        """
        This function informs about SE
        :return:
        """
        information = (f" software engineer named {self.name}, with {self.age}  "
                       f"and position  {self.level}, gets {self.salary} salary")
        return information

    def __str__(self):
        information = (f" how are you software engineer named {self.name}, with {self.age}  "
                       f"and position  {self.level}, gets {self.salary} salary")
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    @staticmethod
    def entry_salary(age):
        """
        If we want a method of a class that is not tied to specific
        instance then we use @static method
        :param age:
        :return:
        """
        if age < 25:
            return 20000
        else:
            return 50000


se_obj1 = SofwareEngineer("pranav", 23, "junior", "30000")
se_obj2 = SofwareEngineer("harsha", 25, "senior", "50000")
se_obj3 = SofwareEngineer("harsha", 25, "senior", "50000")

salary = se_obj1.entry_salary(30)
print(salary)

# print(se_obj2 == se_obj3)


# print(se_obj1)
# print(se_obj2)
# se_obj1.code()
# se_obj2.code()
#
# se_obj1.codes_in_language("python")
# se_obj2.codes_in_language("javascript")
#
# info_1 = se_obj1.information()
# print(info_1)
#
# info_2 = se_obj2.information()
# print(info_2)

# print(f" software engineer named {se_obj1.name}, with {se_obj1.age}  age"
#       f" and position  {se_obj1.level}, gets {se_obj1.salary} salary")
#
# print(se_obj2.name, se_obj2.age, se_obj2.level, se_obj2.salary)
#
# print(f"se1 sits_on = {se_obj1.sits_on}")
# print(f"se2 sits_on = {se_obj2.sits_on}")
# print(f"sits_on = {SofwareEngineer.sits_on}")
#
# print(f"name = {se_obj1.name}")

#recap
# 1)how to write instance methods
# 2)self parameter
# 3)method that takes parameter, that returns parameter
# 4) special dunder methods __eq__ __str__
# 5)@staticmethod