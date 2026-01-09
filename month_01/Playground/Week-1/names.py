
with open("names.txt") as file:
    for line in file:
        names = [line.rstrip() for line in file]


for name in sorted(names):
    print(f"hello, {name}")