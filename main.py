import Bank
import LibraryBook
import StudentMg
import Employee

print("select your project ")
print("1.Banking project ...")
print("2.Employee management system ....")
print("3.Library management system")
print("4.Student managemanet system......")

choice=int(input("Enter your choice....."))
if choice==1:
    Bank.run()
elif choice==2:
    Employee.run()
elif choice==3:
    LibraryBook.run()
elif choice==4:
    StudentMg.run()
else:
    print("Inviled Choice please select your correct choices..")
print("your program is done complete")                    