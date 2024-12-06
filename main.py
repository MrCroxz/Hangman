import random

def load_words():
    """
    Loads a list of words for the Hangman game.
    """
    return [
        "programming", "developer", "school", "assignment", "game", "python", "java", 
        "javascript", "html", "code", "coding", "computer", "internet", "programminglanguage", 
        "datatypes", "github", "machinelearning", "algorithm", "database", "software", 
        "artificialintelligence", "technology", "innovation", "hardware", "cybersecurity"
    ]  # Returns a list of words that can be used in the game.

def display_word(word, guesses):
    """
    Displays the current state of the word with guessed letters revealed.
    """
    return " ".join([letter if letter in guesses else "_" for letter in word])  # Creates a string where guessed letters are shown, and others are "_".

def display_hangman(mistake_count):
    """
    Displays the hangman based on the number of incorrect guesses.
    """
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    print(stages[mistake_count])  # Displays the hangman based on the number of incorrect guesses.

def hangman():
    """
    Main function that runs the game.
    """
    print("Welcome to Hangman!")  # Welcome message.
    print("----------------------")

    word_list = load_words()  # Loads a list of words.
    word = random.choice(word_list).lower()  # Chooses a random word.
    guesses = set()  # Creates a set to track correct guesses.
    incorrect_guesses = set()  # Creates a set to track incorrect guesses.
    max_attempts = 6

    while True:
        display_hangman(len(incorrect_guesses))  # Displays hangman for incorrect guesses.
        print("\n" + display_word(word, guesses))  # Displays the word with guessed letters revealed.
        print(f"Incorrect guesses: {' '.join(sorted(incorrect_guesses))}")
        print(f"Remaining attempts: {max_attempts - len(incorrect_guesses)}")

        if set(word).issubset(guesses):  # All letters in the word have been guessed.
            print("\nCongratulations! You guessed the word:", word)
            break 

        if len(incorrect_guesses) >= max_attempts:  # Used up all attempts.
            display_hangman(len(incorrect_guesses))  # Displays the full hangman.
            print("\nGame over! The word was:", word)
            break  

        guess = input("\nGuess a letter: ").lower() 
        if not guess.isalpha() or len(guess) != 1:  # Checks that the guess is a valid letter.
            print("Please enter a single valid letter.")
            continue 

        if guess in guesses or guess in incorrect_guesses:  # Checks if the letter has already been guessed.
            print("You already guessed that letter.")
            continue 

        if guess in word:  # Checks if the guess is correct.
            guesses.add(guess)  # Adds the letter to the set of correct guesses.
            print(f"Good guess! {guess} is in the word.") 
        else:  # If the guess is incorrect.
            incorrect_guesses.add(guess)  # Adds the letter to the set of incorrect guesses.
            print(f"Wrong guess! {guess} is not in the word.")

    print("\nThank you for playing Hangman!")

if __name__ == "__main__":
    hangman()
