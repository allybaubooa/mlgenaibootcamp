from anagram_checker import AnagramChecker as ac

def show_menu():
    print("\n===== ANAGRAM CHECKER =====")
    print("1) Enter your word: ")
    print("2) Exit the Application...")

def get_word():
    user_input = input("Enter your word: ").strip()

    single_word = user_input.split()
    if len(single_word) != 1:
        print("Error: Please Enter only a single word with no spaces!!!")
        return None
    
    word = single_word[0]

    if not word.isalpha():
        print("Error: Please Enter only word with alphabetic characters! No number or symbols are allowed.")
        return None
    
    return word

def main():
    checker = ac()

    while True:
        show_menu()
        choice = input("Choose an option (1 or 2): ").strip()

        if choice == "2":
            print("Goodbye!")
            break
        
        elif choice == "1":
            word = get_word()
            if word is None:
                continue 

            print(f'\nYOUR WORD : "{word.upper()}"')

            if checker.is_valid_word(word):
                print("This is a valid English word.")
                anagrams = checker.get_anagrams(word)

                if anagrams:
                    print("Anagrams for your word:", ", ".join(anagrams) + ".")
                else:
                    print("Anagrams for your word: (none found).")
            else:
                print("This is NOT a valid English word.")

        else:
            print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()