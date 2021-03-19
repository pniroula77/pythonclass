class Employee:

  # class variables
  raise_amount = 1.04

  def __init__(self, first, last, pay): # sort of a constructor
    self.first = first 
    self.last = last
    self.pay = pay
    self.email = first + "." + last + "@comapny.com"

  def fullname(self): # class method
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
  raise_amount = 1.10

  def __init__(self, first, last, pay, prog_lang):
    super().__init__(first, last, pay) # send these attributes to the super(parent) class of the current class 
    self.prog_lang = prog_lang

class Manager(Employee):

  def __init__(self, first, last, pay, employees=None):
    super().__init__(first, last, pay) # send these attributes to the super(parent) class of the current class 
    
    if employees == None:
      self.employees = []
    else:
      self.employees = employees

  def add_employee(self, emp):
    if emp not in self.employees:
      self.employees.append(emp)  

  def remove_employee(self, emp):
    if emp in self.employees:
      self.employees.remove(emp)

  def print_employees(self):
    for emp in self.employees:
      print("-->", emp.fullname())


dev_1 = Developer("Farrukh", "Rasool", 75000, "Python")
dev_2 = Developer("Zoraiz", "Qureshi", 60000, "C++")
mgr_1 = Manager("Sue", "Smith", "150000", [dev_1])

# mgr_1.print_employees()
mgr_1.remove_employee(dev_1)
mgr_1.print_employees()