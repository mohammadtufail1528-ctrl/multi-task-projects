

class Bank():
    def __init__(self,Account_Numebr,Holder_Name,Balance):
        self.Account_Number=Account_Numebr
        self.Holder_Name=Holder_Name
        self.__Balance=Balance
    def display(self):
            print(f"Your Account_Numebr is :{self.Account_Number}")
            print(f"Your Account_Holder_Name is :{self.Holder_Name}")
            print(f"Your Account_Balnace  is :{self.__Balance}")
    def set_deposit(self,amount):
            self.__Balance+=amount
    def get_deposite(self):
            return self.__Balance
        
    def set_widthral(self,amount):
            self.__Balance-=amount
    def get_widthral(self):
            return self.__Balance

def run(): 
            
 Ac1=Bank(512401004532,"Sariyakhan",2000)
 Ac2=Bank(512510002323,"Adilkhan",3000)
 Ac3=Bank(512510002333,"BabarKhan",4000)
 Ac4=Bank(512510002443,"Shibukhan",3000)
 Ac5=Bank(5125100023343,"RustamAli",3000)
    
 for bank in [Ac1, Ac2,Ac3,Ac4,Ac5]:
    bank.display()
    bank.set_deposit(6000)
    print("After  deposited your Account balance is:-",bank.get_deposite())
    bank.set_widthral(3000)
    print("After widthral your Account balance is:-",bank.get_widthral())
    print("---------------------------------")
    
    