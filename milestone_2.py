import random

word_list = ["strawberry", "raspberry", "orange", "kiwi", "cherry"]

word = random.choice(word_list)

if __name__ == '__main__':

    guess = (input("Please enter a single letter:"))


    if len(guess.lower()) == 1 and guess.lower().isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a valid input")

