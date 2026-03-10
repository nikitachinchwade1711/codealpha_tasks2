import random

# List of predefined words for the game
word_list = ["python", "coding", "alpha", "game", "logic"]

def hangman():
    # Choose a random word
    word = random.choice(word_list)
    word_length = len(word)
    
    # Initialize display word with underscores
    display = ["_" for _ in range(word_length)]
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to the Hangman Game!")
    print("Guess the word one letter at a time.")
    print("You have 6 incorrect attempts allowed.")
    print(" ".join(display))

    while incorrect_guesses < max_attempts:
        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            for i in range(word_length):
                if word[i] == guess:
                    display[i] = guess
            print(" ".join(display))
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! Attempts left: {max_attempts - incorrect_guesses}")

        # Check if the word is fully guessed
        if "_" not in display:
            print("Congratulations! You guessed the word.")
            break
    else:
        print(f"Game over! The word was '{word}'.")

# Run the game
hangman()
