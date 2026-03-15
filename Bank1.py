class Account():
    def __init__(self,account_number, holder_name,balance):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=balance
    def dispaly(self):
        print("------- your persional Bank Details-------")
        print("your account_number is:=",self.account_number)
        print("your account_holder_name is:=",self.holder_name)
        print("Your account balance is:=",self.balance)
    def deposite(self,amount):
        self.balance+=amount
        print(f"Rupee:{amount} is deposted Successfully....")
        
    def widthral(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Rupee: {amount}is widthral Successfull...")
        else:
            print("insufficient balance......")    
            
class SavingAccount(Account):
    def __init__(self, account_number, holder_name, balance,intrest_rate):
        super().__init__(account_number, holder_name, balance)
        self.intrest_rate=intrest_rate
    def  add_rate(self):
            intrest=self.balance*self.intrest_rate/100
            self.balance+=intrest
            print(f"intrest_rat is:={intrest} add to Account ..")
class CurrentAccount(Account):
    def __init__(self, account_number, holder_name, balance ,overdraftlimit):
        super().__init__(account_number, holder_name, balance)
        self.overdraftlimit=overdraftlimit
    def widthral(self, amount):
        if amount<= self.balance+self.overdraftlimit:
            self.balance-=amount
            print(f"overdraftlimit is{amount}is add to account Successfully ...")
        else:
            print("Overdraft limit exceeded")    
                   
saving=SavingAccount(12343212,"shibukhan",3233,10)
        
saving.dispaly()
saving.deposite(4000)
saving.add_rate()
saving.widthral(2000)
print("--------Your current acount balnce is------")
saving.dispaly()

print("\n-------------------")

print("Your CurrentAccount overdfratbalance ralted informations here.....")

currenaccount=CurrentAccount(635252532,"Serekhan",5000,3000)
currenaccount.dispaly()
currenaccount.widthral(7000)


currenaccount.dispaly() 
        