class BankAccount :

    # Encapsulation :
    def __init__(self ,owner ,balance=0):
        self.owner=owner              # public 
        self._balance =balance        # private ._balance
    def deposite (self,amount):
        if amount <=0 :
            raise ValueError("deposite amount must be postive number ")
        self._balance+=amount
    def withdraw (self ,amount):
        if amount <=0 :
            raise ValueError("withdraw amount must be postive number ")
        if amount > self._balance :
            raise ValueError ("Insufficient founds ")
        self._balance-=amount
    def get_balance (self) :
        return self._balance   

# create object 
account= BankAccount("kerolos",100)
account.deposite(50)
account.withdraw(20)
print(account.get_balance())