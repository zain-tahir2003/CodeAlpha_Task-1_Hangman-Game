import random

def choose_word():
    words = {
        "animals": ["dog", "cat", "elephant", "tiger", "lion"],
        "fruits": ["apple", "banana", "orange", "grape", "kiwi"],
        "colors": ["red", "blue", "green", "yellow", "orange"],
        "countries": ["india", "usa", "china", "russia", "japan"]
    }
    category = random.choice(list(words.keys()))
    return category, random.choice(words[category])

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word

def display_hangman(wrong_attempts):
    stages = [
        """
        _______
        |     |
        |
        |
        |
        |
        -
        """,
        """
        _______
        |     |
        |     O
        |
        |
        |
        -
        """,
        """
        _______
        |     |
        |     O
        |     |
        |
        |
        -
        """,
        """
        _______
        |     |
        |     O
        |    /|
        |
        |
        -
        """,
        """
        _______
        |     |
        |     O
        |    /|\\
        |
        |
        -
        """,
        """
        _______
        |     |
        |     O
        |    /|\\
        |    /
        |
        -
        """,
        """
        _______
        |     |
        |     O
        |    /|\\
        |    / \\
        |
        -
        """
    ]
    return stages[wrong_attempts]

def play_hangman():
    category, word = choose_word()
    guessed_letters = []
    max_attempts = 6
    wrong_attempts = 0
    guesses = 0

    print("Welcome to Hangman!")
    print("Try to guess the word from the category '{}'.".format(category.capitalize()))
    print("You have {} chances to guess incorrectly.".format(max_attempts))
    print("Hint: The word belongs to the category '{}'.".format(category.capitalize()))

    while wrong_attempts < max_attempts:
        print("\n" + display_hangman(wrong_attempts))
        print(display_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)
        guesses += 1

        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You've guessed the word '{}' correctly!".format(word))
                print("Total guesses: ", guesses)
                break
        else:
            print("Incorrect guess.")
            wrong_attempts += 1

    if wrong_attempts == max_attempts:
        print("\nSorry, you've run out of attempts. The word was '{}'.".format(word))

if __name__ == "__main__":
    play_hangman()
