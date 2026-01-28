import pandas

data = pandas.read_csv("//home//vimal-prasath//Learning-ml-2026//month_01//Playground//Week-3//Squirrel//Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

final_table = {"Fur Color": ["Grey","Cinnamon", "Black"], 
               "Count": [gray_squirrels, Cinnamon_squirrels, Black_squirrels]}

DFile = pandas.DataFrame(final_table)
DFile.to_csv("Final")
