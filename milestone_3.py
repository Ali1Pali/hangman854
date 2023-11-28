from milestone_2 import word as secret_word

def check_guess(guess):
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again")

def ask_for_input():
    while True:
        guess = input("Choose a letter:")
        if guess.isalpha() and len(guess) == 1:
          break
        else:
            print("Invalid letter. Please enter as single alphabetic character")
    check_guess(guess)
ask_for_input()