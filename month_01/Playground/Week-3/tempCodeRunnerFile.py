class Laptop:
    def __init__(self,Ram,Processor,Cost,Bank_balance):
        self.Ram = Ram
        self.Processor = Processor 
        self.Cost = int(Cost)
        self.Bank_Balance = int(Bank_balance)
    def __str__(self):
        return f"{self.Ram} with {self.Processor} will cost you {self.Cost}"
    
    def Get_Laptop(self):
        if self.Bank_Balance < self.Cost :
            print(f"Go earn some money, need {self.Cost - self.Bank_Balance}")
        else: 
            print(f"You got laptop and here is your remaining amount {self.Bank_Balance - self.Cost}")


        

Cheap_L = Laptop("10GB", "intel_i3", "10_000", Bank_balance = input("Bank_Balance: "))

Costly_L = Laptop("32GB", "intel_i9", "120000", 300)

Cheap_L.Bank_Balance = 100000000
print(Cheap_L)
print("Do you need Laptop?")
Cheap_L.Get_Laptop()




