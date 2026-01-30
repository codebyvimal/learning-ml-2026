class Rocket:
    def __init__(self,name,fuel):
        if not name:
            raise ValueError("Rocket must have a name")
        if  int(fuel) < 0 or int(fuel) > 100:
            raise ValueError("Fuel must be 0-100")
        else:
            self.name = name
            self.__fuel = int(fuel)


    def __str__(self):
        return f"{self.name} is ready with {self.__fuel}% fuel"

    
    def launch(self):
        if self.__fuel >= 10:
            print("3... 2... 1... Blastoff!")
            self.__fuel = self.__fuel-10
        elif self.__fuel < 10:
            print("Mission aborted. Low fuel.")



def MakeRocket():
    name = input("Name: ")
    _fuel = input("Fuel: ")
    return Rocket(name,_fuel)

def main():
    WrongRocket = Rocket("Nasa",50)
    WrongRocket.__fuel = 200
    print(WrongRocket.__fuel)
    print(WrongRocket)
    WrongRocket.launch()
    print(WrongRocket.__dict__)

main()

