#import csv
#
#with open("weather_data.csv") as file:
#    Read = csv.reader(file)
#    temperatures = []
#    next(Read)
#    for line in Read:
#        temperatures.append(int(line[1]))
#    
#    print(temperatures)
 #lets use pandas

import pandas

#data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#data_dict = data.to_dict()
#temp_list = data["temp"].to_list()
#print(data.temp)
 # print row
#print(type(data[data.temp == data.temp.max()]))
#monday = data[data.day == "Monday"]
#print(monday.condition.item())

# Creating a dataframe from scratch
#data_dict = {"students": ["Amy", "James", "Vimal"],
             #"gender": ["female", "male", "male"]}
#data = pandas.DataFrame(data_dict)
#print(data)
#data.to_csv("New_CSV")

#data = pandas.read_csv("Squirrel_Data.csv")
#gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
#Cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
#Black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
#
#final_table = {"Fur Color": ["Grey","Cinnamon", "Black"], 
#               "Count": [gray_squirrels, Cinnamon_squirrels, Black_squirrels]}

#DFile = pandas.DataFrame(final_table)
#DFile.to_csv("Final")

#data = pandas.read_csv("Squirrel_Data.csv")
#chosen_one = (data[data["Unique Squirrel ID"] == "8H-AM-1017-06"])
#x = chosen_one["Age"].item()
#print(x)