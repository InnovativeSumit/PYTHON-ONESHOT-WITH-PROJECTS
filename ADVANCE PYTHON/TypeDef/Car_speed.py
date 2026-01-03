from typing import Union

class Car:
    def __init__(self, name:str, model:str, cost:Union[int,float])->None:
     self.name:str =name
     self.model:str = model
     self.cost:Union[int,float] = cost
     self.speed:int=0
     print(f"{self.name}, {self.model}, ₹{self.cost}")
     
    def speedup(self,speed):
        if(speed<0):
            print("Not possible")
        elif(speed == 0):
            print("That also not possible")
        else:
            self.speed+=speed
            print(f"{speed} increased")
            print(f"Now the total speed is {self.speed}")
    
    def speedown(self,speed):
        if(speed<0):
            print("Not possible")
        elif(speed >self.speed ):
            print("That also not possible")
        else:
            self.speed-=speed
            print(f"{speed} decreased")
            print(f"Now the total speed is {self.speed}")
    
car1=Car("BMW"," electric cars (iX, i4, i7)",9000000.89)
car1.speedup(20)
car1.speedown(10)
car1.speedup(80)
car1.speedown(30)



