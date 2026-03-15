
class StudenManagement():
    def __init__(self,Roll,Name,Subject,marks):
        self.Roll=Roll
        self.Name=Name
        self.Subject=Subject
        self.marks=marks
    def dispaly(self):
        print(f"your roll number is :{self.Roll}")
        print(f"your name is :{self.Name}")
        print(f"your Subject  is :{self.Subject}")
        print(f"your marks outoff 600/{self.marks}")
        
        
    def calculate(self):
        if self.marks>=589:
            return "Grade +A"
        elif self.marks>=544:
            return "Grade A"
        elif self.marks>=450:
            return "Greade B"
        elif self.marks>=400:
            return "Grade C"
        else:
            return "failse"    
        
def run():
 print("4.Student Management project is running......")       
 s1=StudenManagement(1,"Shibukhan","'math','english','Hindi','Urdu','Science'",589)
 s2=StudenManagement(2,"Shibukhan","'math','english','Hindi','Urdu','Science'",566)
 s3=StudenManagement(3,"Shibukhan","'math','english','Hindi','Urdu','Science'",450)
 s4=StudenManagement(4,"Shibukhan","'math','english','Hindi','Urdu','Science'",400)
 s5=StudenManagement(5,"Shibukhan","'math','english','Hindi','Urdu','Science'",350)

 for student in [s1,s2,s3,s4,s5,]:
    student.dispaly()
    
    print(student.calculate())
    print("---------------------------")
       
       
        
        
        
        