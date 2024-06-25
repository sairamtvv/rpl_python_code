# encapsulation
# mechanism of hiding data implementation
#instance variables are kept private


#There is only one accessor method from  outside to acces them.
class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = 0
        self._num_bugs_solved = 100
    @property
    def salary(self):
        return self._salary

    # def get_salary(self):
    #     return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = self._calculate_final_salary(value)


    # def set_salary(self, value):
    #     self._salary = self._calculate_final_salary(value)

    def _calculate_final_salary(self,value):
        base_value = self._set_base_salary(value)
        real_salary = self._calculate_salary(base_value)
        return real_salary

    def _set_base_salary(self, base_value):
        if base_value <= 10000:
             return 10000
        elif base_value > 200000:
             return 200000

    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3




se1 = SoftwareEngineer("pranav", 25)

se1.salary = 10000
#se1.set_salary(10000)
# print(se1.get_salary())
print(se1.salary)


#recap
1) encapsulation
2) abstraction
3) public private
4) getter setter
5) @property @setter

# print(se1.name, se1.age)