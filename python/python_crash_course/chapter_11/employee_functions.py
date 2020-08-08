class Employee:

    def __init__(self, first, last, annual_salary):
        self.first = first
        self.last = last
        self.annual_salary = annual_salary
    
    def give_raise(self, new_amount=5000):
        self.annual_salary += new_amount