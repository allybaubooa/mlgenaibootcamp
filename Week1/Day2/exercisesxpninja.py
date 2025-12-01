# Exercise 1 : Use the terminal

# The PATH variable is a list of directories that the shell searches to find executable programs. 
# When you type a command like python3, the system looks through the directories in PATH and runs the first matching executable it finds. 
# This allows you to run programs without being in their actual installation directory.

# Exercise 2 : Alias

# An alias is simply a shortcut you create in your terminal to make long commands easier to type. 
# Instead of writing something like python3 every time, you can set an alias so that typing py runs the exact same command. 
# It’s basically giving a command a small nickname so you can work faster. 
# For example, if you type alias py="python3", the terminal will launch Python whenever you type py. It's a quick way to save time and avoid repeating long commands.
# ref: https://linuxize.com/post/how-to-create-bash-aliases/

# Exercise 3 : Outputs

# 3 <= 3 < 9
# Answer : True; 3 <= 3 is True and 3 < 9 is True.

# 3 == 3 == 3
# Answer : True

# bool(0)
# Answer : False; 0 is False and 1 is True

# bool(5 == "5")
# Answer : False; one int and the other one str

# bool(4 == 4) == bool("4" == "4")
# Answer : True; Both sides are True

# bool(bool(None))
# Answer : False

# x = (1 == True)
# y = (1 == False)
# a = True + 4
# b = False + 10

# Answer : 
x = (1 == True)
y = (1 == False)
a = 1 + 4
b = 0 + 11

print("x is ", x)
print("y is ", y)
print("a: ", a)
print("b: ", b)

# Exercise 4 : How many characters in a sentence ?

my_text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum.'''

print(len(my_text))

# Exercise 5: Longest word without a specific character

long_sentence = ""

while True:
    sentence = input("Write a sentence without the character 'A' (type 'exit' or 'quit' to quit): ")

    if sentence.lower() == 'exit' or sentence.lower() == 'quit':
        print(f"Your sentence was: {long_sentence}")
        break

    if "A" in sentence:
        print("Your sentence contains 'A'!! Try Again.")
        continue
    
    if len(sentence) > len(long_sentence):
        long_sentence = sentence
        print(f"Good Job! Your new longest sentence is: {long_sentence}")
    else:
        print("Not longer than the one before. Keep Trying!!")
