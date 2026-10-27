
import random

# Words for the game
words = ["Tahreem", "apple", "mango", "school", "laptop"]

# Select a random word
secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("================================")
print("       HANGMAN GAME")
print("================================")

while wrong_guesses < max_attempts:

    # Show the word with hidden letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts left:", max_attempts - wrong_guesses)

    # Check win condition
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You Win!")
        break

    guess = input("Guess one letter: ").strip().lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one alphabetic letter.")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame Over!")

print("Secret word:", secret_word)
print("Thanks for playing!")
