# Exercises XP

# Exercise 1: Favorite Numbers

my_fav_numbers = {1, 5, 6, 10, 14, 22, 26}

my_fav_numbers.add(71)
my_fav_numbers.add(46)

my_fav_numbers.remove(46)

friend_fav_numbers = {1, 6, 56, 99, 121}

fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(f"My favorite numbers are: {my_fav_numbers}.")
print(f"My Friend's favorite numbers are: {friend_fav_numbers}.")
print(f"Our favorite numbers are: {fav_numbers}.")

#  Exercise 2: Tuple

t = (1, 6, 5, 8)

# Tuples in Python are immutable, meaning you cannot change them after creation, so trying to add more integers using methods like append() 
# or by assigning a new value to an index will cause an error; the only way to “add” items is by creating a new tuple using concatenation, 
# such as new_tuple = old_tuple + (4, 5), which does not modify the original tuple but returns a completely new one.

# Exercise 3: List Manipulation

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")

apple_count = basket.count("Apples")
print(f"No of Apples: {apple_count}")

basket.clear()

print(f"My basket: {basket}")

# Exercise 4: Floats

# Recap: What is a float? 
# Floats are point numbers such as 3.6, 103.98…

# What’s the difference between a float and an integer?
# Integers are whole numbers such as 1, 14 whereas Floats are point numbers such as 3.6.

mixed_types = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

sequence_numbers = []
for i in range(15, 51, 5):
    sequence_numbers.append(i / 10)

print(sequence_numbers)


#  Exercise 5: For Loop

for i in range(1,21):
    print(i)

for i in range(1,21):
    if i % 2 == 0:
        print(i)

# Exercise 6: While Loop

while True:
    name = input("Enter your name: ")

    if not name.isdigit() and len(name) >= 3:
        print(f"Thank you, Your name is {name}.")
        break
    else:
        print("Invalid name, Try again!")

# Exercise 7: Favorite Fruits

favorite_fruits =  input("Enter your favorite fruits (separated by spaces: ").split()

chosen_fruit = input("Enter the name of any fruit: ")

if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# Exercise 8: Pizza Toppings

toppings = []

while True:
    topping = input("Enter your pizza toppings: ")

    if topping.lower() == 'quit':
        break

    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

base_price = 10
topping_price = 2.5
total = base_price + (len(toppings) * topping_price)

print(f"\nYour Toppings: {toppings}")
print(f"Total cost of the pizza is ${total}")

# Exercise 9: Cinemax Tickets

total_cost = 0

while True:
    age = input("Enter your age(type 'finish when you are done'): ")

    if age.lower() == 'finish':
        break
    
    age = int(age)

    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15

    total_cost += cost

print(f"Total ticket cost: ${total_cost}")

# Bonus:

names = []
allowed_people = []

while True:
    name = input("Enter the person's name (or type 'done' to finish): ")
    if name.lower() == "done":
        break

    age = int(input(f"Enter {name}'s age: "))

    names.append(name)

    if 16 <= age <= 21:
        allowed_people.append((name, age))


print("\nAllowed attendees:")
for person, age in allowed_people:
    print(f"{person} ({age} years old)")
    

