
class Employee():
    def __init__(self,name,Id,basic_salary):
        self.name=name
        self.id=Id
        self.__basic_salary= basic_salary
    def dispaly_details(self):
        print(f"emp_name is:-{self.name}")
        print(f"emp_id is:-{self.id}")
        print(f"emp_Salary is :-",self.__basic_salary)
    def set_update_salary(self,newsalary):
            self.__basic_salary=newsalary
    def get_salary(self):
        return self.__basic_salary
def run():
 print("2.Employee is running.....",end="")    
 
 emp= Employee("shibukhan",1,34000)
 emp.dispaly_details()    
 emp.set_update_salary(6000)
 print("new update_salary is :-",emp.get_salary())



        