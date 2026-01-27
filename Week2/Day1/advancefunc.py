people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

short_names = filter(lambda n: (len(n) <=4), people)

greetings = map(lambda n: f"Hello {n}", short_names)

for i in greetings:
    print(i)