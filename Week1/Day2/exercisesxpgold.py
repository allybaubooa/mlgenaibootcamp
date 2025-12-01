# Exercises XP Gold

# Exercise 1 : Hello World-I love Python
print("Hello world\nHello world\nHello world\nHello world\nI love python\nI love python\nI love python\nI love python")

# Exercise 2 : What is the Season ?

month = int(input("Input your Month here (1 to 12): "))

if 3 <= month <= 5:
    print("It's Spring Time!! The flowers are blooming")
elif 6 <= month <= 8 :
    print("Time to go to the beach! Summer is here!")
elif 9 <= month <= 11 :
    print("Well time to clean the Garden! There are leafs eveywhere. Autumn is here!!")
elif month == 12 or 1 <= month <= 2 :
    print("Hot Chocolate, A good Christmas movie! Lets have a great Winter!")
else:
    print("Please enter a valid month!")
