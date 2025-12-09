# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
import random

def play_hangman():
    # 1. SETUP: List of 5 predefined words
    word_list = ["python", "guitar", "jungle", "rocket", "wizard"]
    
    # Select a random word from the list
    secret_word = random.choice(word_list)
    
    # Create a list of underscores to represent the hidden word
    # Example: If word is "python", display is ['_', '_', '_', '_', '_', '_']
    display_word = ["_"] * len(secret_word)
    
    lives = 6
    guessed_letters = [] # To keep track of what the user has already typed

    print("--- Welcome to Hangman! ---")
    print(f"I have chosen a word with {len(secret_word)} letters.")
    
    # 2. GAME LOOP: continues as long as player has lives AND hidden letters remain
    while lives > 0 and "_" in display_word:
        print("\n" + "-" * 20)
        print(f"Lives remaining: {lives}")
        print(f"Guessed so far: {', '.join(guessed_letters)}")
        print("Word: " + " ".join(display_word)) # Join list into a string for display
        
        # Get user input
        guess = input("Guess a letter: ").lower()

        # Input Validation (check if it's a single letter)
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if already guessed
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different one.")
            continue
        
        guessed_letters.append(guess)

        # 3. CHECK GUESS logic
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
            
            # Loop through secret word to find all occurrences of the letter
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    display_word[index] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            lives -= 1

    # 4. END GAME: Check win or loss condition
    print("\n" + "-" * 20)
    if "_" not in display_word:
        print(f"Congratulations! You guessed the word: {secret_word}")
    else:
        print(f"Game Over! You ran out of lives.")
        print(f"The word was: {secret_word}")

# Run the game
play_hangman()