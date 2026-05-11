import random

words = ["apple", "tiger", "table", "pizza", "beach"]

chosen_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_guesses:

    display_word = ""

    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")

    elif guess in chosen_word:
        print("Correct guess!")
        guessed_letters.append(guess)

    else:
        print("Wrong guess!")
        wrong_guesses += 1
        guessed_letters.append(guess)
        print("Remaining guesses:", max_guesses - wrong_guesses)

if wrong_guesses == max_guesses:
    print("\nYou lost!")
    print("The word was:", chosen_word)
