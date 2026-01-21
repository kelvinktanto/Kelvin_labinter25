word_list = "python"

print("H A N G M A N")
print("Welcome to Hangman!")
print("Guess the word:")
print("You have 6 attempts to guess the word.")

attempts = 6
guesses = set()

while attempts > 0:
    display_word = "".join(letter if letter in guesses else "-" for letter in chosen_word)
    print("\n" + display_word)
    if display_word == chosen_word:
        print("You guessed the word!")
        print("You survived!")
        break

    guess = input("Input a letter: ")
    if len(guess) != 1:
        print("You should input a single letter")
        continue
    if not guess.isalpha() or not guess.islower():
        print("Please enter a lowercase English letter")
        continue
    if guess in guesses:
        print("You've already guessed this letter")
        continue

    guesses.add(guess)
    if guess not in chosen_word:
        print("That letter doesn't appear in the word")
        attempts -= 1
        print(f"You have {attempts} attempts left.")
else:
    print("You lost!")
    print(f"The word was: {chosen_word}")


