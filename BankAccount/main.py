class BankAccount :
    """A simple bank account with safe deposits and withdrawals."""
    # ---------- Data ----------
    def __init__(self ,owner : str ,balance:float=0):
        self.owner=owner              # public 
        self._balance =balance        # private .__balance  protect and have access on the childs
        
    # ---------- Read-only property ---------
    @property
    def balance (self) -> float :
        """Read-only access to the balance"""
        return self._balance  
    
    # ---------- Behaviors ----------
    def deposite (self,amount:float)-> None :
        if amount <=0 :
            raise ValueError("deposite amount must be postive number ")
        self._balance+=amount
    def withdraw (self ,amount:float)-> None :
        if amount <=0 :
            raise ValueError("withdraw amount must be postive number ")
        if amount > self._balance :
            raise ValueError ("Insufficient founds ")
        self._balance-=amount
    
    # ---------- Dunder method  ----------
    def __str__ (self) -> str :
        return f"Account information owner and Class name : {self.__class__.__name__} ({self.owner} , Balance = {self.balance})"


class SavingsAccount (BankAccount): 
    """A bank account that earns interest over time."""
    def __init__(self ,owner :str ,balance : float =0 , interest_rate :float =0.05 ):
        super().__init__(owner,balance)   # Call parent's __init__method 
        self.interest_rate =interest_rate

    def add_interest(self)-> None :   # a new method for the child class 
        self._balance +=self._balance * self.interest_rate

class CheckingAccount(BankAccount):
    """A bank account that allows withdrawing more than the balance (overdraft)."""
    def __init__(self , owner : str , balance : float =0 ,overdraft_limit : float = 500) :
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit 

    # New Rules but the same method "Overriding"
    def withdraw (self,amount : float)-> None : 
        if amount <=0 :
            raise ValueError ("Withdraw must be positive")    
        if amount > self._balance + self.overdraft_limit :
            raise ValueError ("Overdraft limit exceeded")
        self._balance-=amount

#Polymorphism Example  --> many forms 
accounts =[
    BankAccount("Kerolos", 2000),
    SavingsAccount("Amgad",1000,0.05),
    CheckingAccount("Elias",100 ,overdraft_limit=300)
]

if __name__ =="__main__":
    for acc in accounts :
        print(acc)
        acc.deposite(500)
        acc.withdraw(200)
        print(f"Final balance after operations : {acc.balance}")
