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
print(data["temp"])