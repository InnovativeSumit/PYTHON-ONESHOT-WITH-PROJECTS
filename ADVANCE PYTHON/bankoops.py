from typing import Union
class Bank:
    def __init__(self, name: str, age: int, isMarried: bool) -> None:
        self.name: str = name
        self.age: int = age
        self.isMarried: bool = isMarried
        self.amount: Union[int, float] = 0
        print(f"The name is {self.name}, age is {self.age}, married status is {self.isMarried}")

    def addAmount(self, amount: Union[int, float]) -> None:
        if amount <= 0:
            print("Amount must be positive")
            return
        self.amount += amount
        print(f"₹{amount} added successfully")
        print(f"Total balance is ₹{self.amount}")

    def withdraw(self, amount: Union[int, float]) -> None:
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.amount:
            print("Insufficient balance ")
        else:
            self.amount -= amount
            print(f"₹{amount} withdrawn successfully ")
            print(f"Remaining balance is ₹{self.amount}")

    
        
user = Bank("sumit", 89, False)
user.addAmount(1000)
user.withdraw(500.90)

