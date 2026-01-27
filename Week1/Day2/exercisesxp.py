# Exercise 1: Hello World

for i in range(4): print("Hello world")

# Exercise 2: Some Math

result = (99**3) * 8

print("Exercise 2 Result: ",result)

# Exercise 3: What is the output?

# 5 < 3 : False
# 3 == 3 : True
# 3 == "3" : False
# "3" > 3 : TypeError
# "Hello" == "hello" : False

#  Exercise 4: Your computer brand
computer_brand = "Asus VivoBook"

print(f"I have a {computer_brand} computer")

# Exercise 5: Your information

name = "Ally"
age = 27
shoe_size = 45
info = f"I am {name}. I am {age} years old. I am a Software Engineer.\nFun fact about me is my shoe size is {shoe_size}."

print(info)

# Exercise 6: A & B

a = 26 ; b = 22

if a > b:
    print("Hello World")

# Exercise 7: Odd or Even

number = int(input("Please enter a number: "))

if number % 2 == 0:
    print(f"{number} is an even number")
else :
    print(f"{number} is an odd number")

# Exercise 8: What’s your name?

username = str(input("What’s your name? : "))

if username == name:
    print(f"I am the original {username}!! You impostor.")
else:
    print(f"Hey {username}! Nice name.. But mine's cooler than yours.")

# Exercise 9: Tall enough to ride a roller coaster

user_height = int(input("Please state your height before stepping in the ride(in cm's): "))

if user_height > 145:
    print("Hop on you big fella!😎")
elif user_height <= 145:
    print("Well you clearly have some more inches to grow!! 😂")



