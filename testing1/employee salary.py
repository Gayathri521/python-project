
class Employee:
    def unit_(self,name,salary):
       self.name = name
       self.salary = salary
       self.email = name.lower() + '@hcl.com'
    def apply_raise(self,percentage):`
        self.salary = int(self.salary * (1 + percentage / 100))