import csv

name = input("what's your name?")
place = input("What's your place?")

with open("student.csv","a") as file:
    writer = csv.DictWriter(file, fieldnames = ["name","place"])
    writer.writerow({"name": name, "place": place})