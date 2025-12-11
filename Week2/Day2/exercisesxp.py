# Exercise 1: What Are You Learning?

def display_message():
    print("I am learning about functions in Python.")

display_message()

# Exercise 2: What’s Your Favorite Book?

def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Harry Potter")

# Exercise 3: Some Geography

def describe_city(city, country= "Unknown"):
    print(f"{city} is situated in {country}.")

describe_city("Paris")
describe_city("Rome", "Italy")

# Exercise 4: Random

import random

def compare(number):
    random_number = random.randint(1,100)

    if number == random_number:
        print("Success")
    else:
        print(f"Fail!! Your number: {number}; Random number: {random_number}")

compare(60)

# Exercise 5: Let’s Create Some Personalized Shirts!

def make_shirt(size= "large", text="I love Python"):
    print(f"Your shirt size is {size}. {text}.")

make_shirt("medium", "I Like to move it move it!!")
make_shirt()
make_shirt("medium")
make_shirt("small", "I love Super Mario.")

make_shirt(size="medium", text="Bye!")

# Exercise 6: Magicians…

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(names):
    for magician in names:
        print(magician)

def make_great(names):
    for i in range(len(names)):
        names[i] = "The Great " + names[i]
        

make_great(magician_names)
show_magicians(magician_names)

# Exercise 7: Temperature Advice

import random

def get_random_temp(season):
    if season == "winter":
        return random.uniform(-10, 16)
    elif season == "spring":
        return random.uniform(10, 23)
    elif season == "summer":
        return random.uniform(20, 40)
    elif season == "autumn":
        return random.uniform(10, 24)
    else:
        return random.uniform(-10, 40)


def main():
    month = int(input("Enter the month number (1–12): "))

    if month in (12, 1, 2):
        season = "winter"
    elif month in (3, 4, 5):
        season = "spring"
    elif month in (6, 7, 8):
        season = "summer"
    else:
        season = "autumn"

    temp = round(get_random_temp(season), 1)

    print(f"\nThe temperature right now is {temp}°C.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif temp < 23:
        print("Nice weather.")
    elif temp < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")


# Run the program
main()
