


class Employee():
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first+'.'+last+'@gmail.com'
        self.pay = pay
    @property
    def fullname(self):
        return f"The name is {self.first} {self.last}"

    @fullname.setter    
    def fullname(self,name):
        first, last = name.Split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('name Deleted')
        self.first = None
        self.last = None


       

    def set_first(self,new_first):
        self.first = new_first


class Developer(Employee):
    def __init__(self ,first,last,pay,pro_lang):

        super().__init__(first,last,pay)
        self.pro_lang = pro_lang



class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):

        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_emp(self, emp):
        if emp not in self.employees:
            self.employess.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:

            self.employees.remove(emp)        

    def print_emp(self):
        for emp in self.employees:
            print('----> ' + emp.fullname)

    def __len__(self):
        return len(self.fullname())        

        



emp1 = Employee('ahmed','ali','50')
emp2 = Employee('chmed','ali','50')
emp3 = Employee('sahmed','ali','50')

emp1.fullname = Employee('Moselhi','fff','90')
dev_1 = Developer('Mahmoud', 'ahmed' ,'5000', 'Java')
dev_2 = Developer('Mahmoud', 'kamal' ,'8000', 'PhP')
mang_1 = Manager('abdelrahman','mohamed','78',[dev_2])

print(emp1.email)
print(emp1.fullname) 
print(mang_1.print_emp()) 
print(mang_1.get_first())
print(mang_1.set_first('Ali'))
print(mang_1.get_first())
print(isinstance(emp1,Employee))
print(issubclass(Manager,Developer)) 
print(len(mang_1))     


employeez = [emp1,emp2,emp3]

def e_sort(emp):
    return emp.first

s_employee = sorted(employeez, key = e_sort)
print(s_employee)    

