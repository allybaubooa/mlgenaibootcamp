# Exercise 1: Converting Lists into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

output = dict(zip(keys, values))
# OR
output_2 = {keys[i]: values[i] for i in range(len(keys))}

print(output)
print(output_2)

# Exercise 2: Cinemax #2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for name, age in family.items():
    if age < 3:
        cost = 0
    if 3 <= age <= 12:
        cost = 10
    if age > 12:
        cost = 15
    
    print(f"{name.capitalize()} pays ${cost}")
    total_cost +=cost

print(f"Total cost for family: ${total_cost}")

# Bonus

family= {}
total_cost = 0

while True:
    name = input("Enter member name(type 'done' when all name has been input): ")
    if name.lower() == 'done':
        break

    age = int(input(f"Enter {name} age: "))
    family[name] = age

print("Ticket Prices for each member!!")
for name, age in family.items():
    if age < 3:
        cost = 0
    if 3 <= age <= 12:
        cost = 10
    if age > 12:
        cost = 15
    
    print(f"{name.capitalize()} pays ${cost}")
    total_cost +=cost

print(f"Total cost for family: ${total_cost}")

# Exercise 3: Zara

