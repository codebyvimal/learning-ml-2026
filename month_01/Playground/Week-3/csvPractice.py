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

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
data_dict = data.to_dict()
temp_list = data["temp"].to_list()
print(sum(temp_list)/len(temp_list))
