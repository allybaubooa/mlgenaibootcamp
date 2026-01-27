# def welcome(name,age, title):
#     print(f"My name is {title} {name} and I am {age} years old!")


# welcome("ally", 27, "Mr")
# welcome("noor", 33, "Mrs")
# welcome(age=12, name="Rahul", title="Mrs")

# def calculation(a, b):
#     return a + b, a - b

# addition, substraction = calculation(10, 40)
# print(f"Addition: {addition}")
# print(f"Substraction: {substraction}")

def say_hello(*parameters):
    # print(type(parameters))
    # print(parameters)

    username = parameters[0]    
    if len(parameters) > 1:
        language = parameters[1]
    else:
        language = "EN"

    if language == "EN":
        print("Hello "+username)
    elif language == "FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)

say_hello("Abraham","FR")
say_hello("Ally")
say_hello("Noa","FR","Floreal")