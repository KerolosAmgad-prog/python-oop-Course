class BankAccount :
    """A simple bank account with safe deposits and withdrawals."""
    # ---------- Data ----------
    def __init__(self ,owner ,balance=0):
        self.owner=owner              # public 
        self.__balance =balance        # private .__balance  (encapsulation)
        
    # ---------- Read-only property ---------
    @property
    def balance (self) :
        """Read-only access to the balance"""
        return self.__balance  
    
    # ---------- Behaviors ----------
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
    
    # ---------- Dunder method  ----------
    def __str__ (self):
        return f"Account information owner : {self.owner} , Balance = {self.balance}"

if __name__ =="__main__":
    acc=BankAccount("kerolos",150)
    acc.deposite(50)
    acc.withdraw(30)
    print(acc)    

    try:
        acc.withdraw(1000)
    except ValueError as e:
        print("Error:", e)