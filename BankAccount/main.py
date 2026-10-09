class BankAccount :

    # Encapsulation :
    def __init__(self ,owner ,balance=0):
        self.owner=owner              # public 
        self.__balance =balance        # private .__balance
    
    @property
    def balance (self) :
        """Read-only access to the balance"""
        return self.__balance  

    def deposite (self,amount):
        if amount <=0 :
            raise ValueError("deposite amount must be postive number ")
        self.__balance+=amount
    def withdraw (self ,amount):
        if amount <=0 :
            raise ValueError("withdraw amount must be postive number ")
        if amount > self.__balance :
            raise ValueError ("Insufficient founds ")
        self.__balance-=amount
     

# create object 
account= BankAccount("kerolos",100)
account.deposite(50)
account.withdraw(20)
print(account.balance)