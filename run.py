# Import section
import random
import words
from hangman_stage import stages
import sys
import time
from time import sleep


class txtcolor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Prints the logo & Welcome message
print(txtcolor.HEADER + r"""
  _    _          _   _  _____ __  __          _   _ 
 | |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
 | |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
 |  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
 | |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
 |_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|
""" + txtcolor.ENDC)

welcome_str = """Welcome to the word guessing game where your goal is
to stay ALIVE...\n"""
print(welcome_str)


def display_rules():
    """
    This fuction will display the rules if the user inputs y and skips this
    section if n is inputted
    """
    while True:
        question = input("Would you like to see the rules, y/n?\n")
        if question.lower() == "y":
            typing(txtcolor.HEADER +
                   "\n******************************************************\n"
                   "This is a simple word game, quess one letter at a time.\n"
                   "Guess animal names with 3 difficulty levels:\n"
                   "Easy, medium or hard.\n"
                   "If 6 incorrect letters are guessed, you will be hung.\n"
                   "To win you need to complete the word before being hung.\n"
                   "*******************************************************"
                   + txtcolor.ENDC)
            break
        elif question.lower() == "n":
            break
        else:
            print(txtcolor.WARNING +
                  "\nPlease enter 'y' for yes or 'n' for no. \n"
                  + txtcolor.ENDC)


def users_name():
    """
    This function will ask the user to enter their name, an error will be
    raised where numbers, characters or spaces are entered
    """
    while True:
        try:
            name = input("\nPlease enter your name:\n")
            if not name.isalpha():
                raise ValueError(txtcolor.FAIL +
                                 "Your name can only contain letters."
                                 + txtcolor.ENDC)
            else:
                typing(f"\nReady to play {name.capitalize()}...")
                typing("Good luck!\n")
                break
        except ValueError as err:
            print(err)


def difficulty_level():
    """
    This function allows the user to select between three levels of
    difficulty, easy, medium or hard
    """
    while True:
        try:
            level = input("Choose easy, medium or hard words?\n").lower()
            if level not in ["easy", "medium", "hard"]:
                raise ValueError(txtcolor.FAIL +
                                 "You need to type: easy, medium or hard.\n"
                                 + txtcolor.ENDC)
            elif level == "easy":
                return words.easy_list
            elif level == "medium":
                return words.medium_list
            else:
                return words.hard_list
        except ValueError as err:
            print(err)


def random_word(words_list):
    """
    This function returns a random word of various difficulty from the
    words list
    """
    word = random.choice(words_list)
    return word.upper()


def display_hidden_word(hidden_word, guessed_letters):
    """
    This function displays the random word as underscores, hiding the word from
    the user but displaying the number of letters the hidden word cosists of
    until updated with the correct guessed letters
    """
    blank_word = ""
    # iterate through the hidden word and replace _ with correct letters
    for i in hidden_word:
        if i in guessed_letters:
            blank_word += i
        else:
            blank_word += "_"
    return blank_word


def hangman_stage(guessed_letters, max_attempts):
    """
    This function prints the initial state of the stage and guessed letters
    as well as the updated state throughout the game
    """
    print(stages[max_attempts])
    # accumalates the already guessed letters for the user to refer back to
    print(f"\nGuessed letters: {', '.join(guessed_letters)}\n")


def users_guess(guessed_letters):
    """
    This function request the users to guess a letter, an error is raised
    where anything other than a letter is entered
    """
    while True:
        try:
            guess = input("\nPlease guess a letter: ").upper()
            if not guess.isalpha():
                raise ValueError(txtcolor.FAIL +
                                 "Guess needs to be an alphabetical letter.\n"
                                 + txtcolor.ENDC)
            elif len(guess) > 1:
                raise ValueError(txtcolor.FAIL +
                                 "Your guess can only be one letter.\n"
                                 + txtcolor.ENDC)
            elif guess in guessed_letters:
                raise ValueError(txtcolor.WARNING +
                                 f"You already guessed {guess}, try again.\n"
                                 + txtcolor.ENDC)
            else:
                return guess
        except ValueError as err:
            print(err)


def hangman():
    """
    This function runs the game loop until the word has been guessed or the
    user has been hung and lost the guessing game, feedback is displayed
    to the user throughout
    """
    words_list = difficulty_level()
    hidden_word = random_word(words_list)
    guessed_letters = []
    max_attempts = 0
    word_completion = False

    while max_attempts < 6 and not word_completion:
        hangman_stage(guessed_letters, max_attempts)
        print(" ".join(display_hidden_word(hidden_word, guessed_letters)))
        guess = users_guess(guessed_letters)
        if guess in hidden_word:
            typing(txtcolor.OKGREEN +
                   f"\nCorrect, {guess} is in the secret word!"
                   + txtcolor.ENDC)
            guessed_letters.append(guess)
        else:
            typing(txtcolor.WARNING +
                   f"\nIncorrect, {guess} is not in the secret word."
                   + txtcolor.ENDC)
            max_attempts += 1
            guessed_letters.append(guess)

        updated_word = display_hidden_word(hidden_word, guessed_letters)
        if updated_word in hidden_word:
            word_completion = True

    if word_completion:
        hangman_stage(guessed_letters, max_attempts)
        print(" ".join(display_hidden_word(hidden_word, guessed_letters)))
        typing(txtcolor.OKGREEN +
               f"\nYou WON! {hidden_word} is the secret word!"
               + txtcolor.ENDC)
    else:
        hangman_stage(guessed_letters, max_attempts)
        print(" ".join(display_hidden_word(hidden_word, guessed_letters)))
        typing(txtcolor.WARNING +
               f"\nYou LOSE, {hidden_word} was the secret word..."
               + txtcolor.ENDC)


def play_again():
    """
    This function allows the user to choose to play again or exit if not
    """
    while True:
        question = input("\nWould you like play again, y/n?\n").lower()
        if question.lower() == "y":
            hangman()
        elif question.lower() == "n":
            typing("\nSee you next time!")
            break
        else:
            print(txtcolor.WARNING +
                  "\nPlease enter 'y' for yes or 'n' for no.\n"
                  + txtcolor.ENDC)


def typing(text):
    """
    This fucntion adds the typing effect to my chosen print statements
    """
    words = text
    for char in words:
        time.sleep(0.02)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()


def main():
    """
    This function runs the game loop by displaying the rules, then requesting
    the users name followed by the current game function and finally the
    function to allow the user to exit the gae or play again
    """
    display_rules()
    users_name()
    hangman()
    play_again()


main()
