
with open("names.txt") as file:
    names = [line.rstrip() for line in file]


for name in sorted(names):
    print(f"hello, {name}")