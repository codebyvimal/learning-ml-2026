# I will do some tasks to practice my CSV handling skills
import pandas

data = pandas.read_csv("Pokemon//Pokemon.csv")

# Task 1 - "Create a dataframe that contains only Legendary Pokemon"

# Legendary = data[data.Legendary == True]
# Legendary.to_csv("Legendary_Pokemons.csv")

# Task 2 - "Find all Pokemon where Attack > 100 but Defense < 50. (These are your heavy hitters who die fast)."

separate_pokemons = data[(data.Attack > 100) & (data.Defense < 50)]
separate_pokemons.to_csv("Task-2_Pokemons.csv")
