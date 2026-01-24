#import turtle

#timmy = turtle.Turtle()
#new_screen = turtle.Screen()

#print(new_screen.canvwidth)
#new_screen.exitonclick()

from prettytable import PrettyTable

Table = PrettyTable()
Table.add_column("Pokemon Names", ["Pikachu", "Squirtle", "Charmander"])
Table.add_column("Type", ["Electric", "Water", "Fire"])

print(Table)



