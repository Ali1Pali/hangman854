import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for character in self.word]
        self.num_letters = len(set(self.word))
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        # Checks if guessed letter is in the secret word
        guess = guess.lower()
        self.word = self.word.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word")
        else:
            print(f"Sorry, '{guess}' is not in the word. Try again")

    def ask_for_input(self):
         # Asks for a letter and checks if it is a valid input
        while True:
            guess = input("Choose a letter:")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please enter a single alphabetic character")
            elif guess in self.list_of_guesses:
                print(f"You already tried '{guess}'")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

hangman_attempt = Hangman(["strawberry", "raspberry", "orange", "kiwi", "cherry"])

hangman_attempt.ask_for_input()
