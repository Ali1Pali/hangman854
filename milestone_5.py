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
        guess_lower = guess.lower()
        self.word = self.word.lower()
        if guess_lower in self.word:
            print(f"Good guess! '{guess}' is in the word!")
            for i, character in enumerate(self.word):
                if guess_lower == character:
                    self.word_guessed[i] = character
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
         # Asks for a letter and checks if it is a valid input, and adds the guess to the list of guesses
            guess = input("Choose a letter: ")
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid choice. Please enter a single alphabetic character.")
            elif guess in self.list_of_guesses:
                print(f"You already tried '{guess}'.")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)



def play_game(word_list):
    while True:
        num_lives = 5
        game = Hangman(word_list, num_lives)
        while True:
            if game.num_lives == 0:
                print(f"Unlucky, the word was '{game.word}'. You lose, good day sir!")
                break
            elif game.num_letters > 0:
                game.ask_for_input()
            else:
                print(f"Congratulations. The word was '{game.word}'. You won the game!")
                break
        play_again = False
        while not play_again:
            answer = input("Would you like to play again? Enter Y or N: ")
            if answer.lower() == "y":
                play_again = True
            elif answer.lower() == "n":
                return False
            else:
                print("You did not select Y or N")





play_game(["python", "jumble", "easy", "difficult", "answer", "xylophone"])