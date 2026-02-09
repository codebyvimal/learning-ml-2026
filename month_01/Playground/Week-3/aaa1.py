def laptop(Ram, Processor, Cost):
    return f"{Ram} with {Processor} will cost you {Cost}"


Cheap_L = laptop("10GB", "intel_i3", "10_000")
Costly_L = laptop("32GB", "intel_i9", "1,20,000")

print(Cheap_L)
