import csv

students = []

with open("names.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "place": row["place"]})

for student in sorted(students, key= lambda student: student["name"]):
    print(f"{student['name']} is in {student['place']}")
