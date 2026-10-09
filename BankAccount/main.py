class BankAccount :
    def __init__(self ,owner ,balance=0):
        self.owner=owner
        self.balance =balance
    def deposite (self,amount):
        self.balance+=amount
    def withdraw (self ,amount):
        self.balance-=amount

# create object 
account= BankAccount("kerolos",100)
account.deposite(50)
print(f"balance after deposite {account.balance}")
account.withdraw(20)
print(f"balance after withdraw {account.balance}")