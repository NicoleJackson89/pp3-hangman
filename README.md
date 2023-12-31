# Hangman

### [View the live page here](https://hangman-animals-16cd61b71879.herokuapp.com/)

This Hangman game is Python terminal based and run in the Code Institutes mock terminal on Heroku.

Users can play a solo game of Hangman on one of three difficulty levels, each level has additional letters per word. All words are animal names so this would be a great game for animal lovers.

![Responsive](./assets/docs/am-i-responsive.png)

## How to play

- Hangman is a classic, quick word guessing game perfect to kill some free time or learn a few new words.
- As the user you get the opportunity to choose one of three difficulty levels.
- The objective of this solo game is to guess the hidden word before the stick man is hung.
- Gameplay continues until the figure has been hung (after 6 incorrect guesses) or the word has been correctly guessed, one letter at a time.

## User Experience

In this version of Hangman the user is presented with the classic game where each letter of a word is replaced with a dash (hidden word).  The user will need to guess this word one letter at a time. 

With each correct guess the dash within this word updates and displays the letter in the correct position of the hidden word.

The users goal is to guess the correct word before the game ends, this is displayed with a complete hangman stick figure as well as a message to notify the user that they lost the game.

### Color Palette

- The logo and the rules display as purple.
- Error messages display in red to highlight a problem to the user.
- Correct guess notifications are displayed in green.
- Incorrect guess notifications are displayed in yellow.

### User Stories

#### As a first time visitor I want to:

- Quickly and easily understand how the game works with a clear description of the game objective.
- Navigate the main menu and options available easily.
- Start the game, during game play to recieve messages of correct / incorrect guessed letters.
- Kill time but enjoy the game, left with the idea of wanting to play again.

#### As a returning visitor I want to:

- Easily navigate through the menu and options available.
- Play the game again, with new words to guess and choose different difficulty levels.
- Improve my word skills and become better at guessing words.
- Possibly see updated versions of the game

#### As a frequent visitor I want to:

- Easily navigate through the menu and options available.
- Added word categories or new words added to the game.
- Possibility of playing against another user or AI.
- Challenge myself with harder levels.

## Features

- The main screen: This displays the games name as well as the welcome message followed by an option to view the game rules.
- Game rules: These will be displayed if the user chooses to see them, if not, this step will be skipped.
- Name request: The user is requested to input their name.
- Difficulty options: The user can choose from three options, easy, medium, hard.
- Game display: The hangmans gallows is displayed, the hidden word is displayed with dashes, guessed letters are displayed. these are all updated throughout the progress of the game.
- Correct / Incorrect notification: This is displayed when the user guessed a correct / incorrect letter respectively.
- Guess a letter: The user is requested to guess a single letter.
- Hidden words: These words are randomised from one of the three levels once chosen by the user.
- Play again: This option is given to the user once the game has been won / lost.

### Existing Features

- Main screen

    - Displays the game logo & welcome message:

    ![Logo](./assets/docs/logo-welcome.png)

- Display rules:

    - Gives the user an option to see the rules:

    ![Rules](./assets/docs/rules.png)

    - Rules error displays if the users input is not expected:

    ![Rules error](./assets/docs/rules-error.png)

- User name:

    - Allows the user to enter thier name (Alphabetical letters only)

    ![Name](./assets/docs/user-name.png)

    - User name error:

    ![Name error](./assets/docs/user-name-error.png)

- Difficulty options:

    - Allows the user to choose easy, medium or hard:

    ![Difficulty](./assets/docs/difficulty.png)

    - Error if the option chosen does not exist:

    ![Difficulty error](./assets/docs/difficulty-error.png)

- Game display:

    - The game displays the blank "board" to the user. This displays the hangman gallows, blanked out hidden word, blank guessed letters as well as the request for the user to guess a letter:

    ![Game display](./assets/docs/game-display.png)

- Correct guess:

    - This displays when the user guessed a letter correctly and updates the hidden word:

    ![Correct](./assets/docs/correct.png)

- Incorrect guess:

    - This displays when the user guessed a letter incorrectly and updates the hangmans gallows:

    ![Incorrect](./assets/docs/incorrect.png)

- Errors on guess:

    - This error displays if the user tries to enter anything other than a letter:

    ![Not a letter](./assets/docs/not-letter.png)

    - This error displays if the user enters more than one letter:

    ![More than one letter](./assets/docs/one-letter.png)

- Updated guessed letters list:

    - This updates as the user guesses a new letter:

    ![Guessed letters](./assets/docs/guessed-letters.png)

- Play again:

    - This option becomes available to the user once the game is won / lost:

    ![Play again](./assets/docs/play-again.png)

### Future Features

- Additional words can be added to the word list.
- The option of different word categories can be added for the user to choose from.
- A two player option or an option to play against the computer.

## Flowchart

![Flowchart](./assets/docs/flowchart.png)

## Testing

### CI Python Linter

Function were tested using [CI Python linter](https://pep8ci.herokuapp.com/) throughout the building process of the game, making the fnal testing stage simpler and a smoother process.
![run.py](./assets/docs/run.png)
![words.py](./assets/docs/word-list.png)
![hangman_stage.py](./assets/docs/hangman.png)

### Manual Testing

|What was tested|Result|
|---|---|
|Rules: Should be displayed if "y" is entered or skip if "n" is entered.|Passed|
|Users name error message: Should be one word and only alphabetical letters.|Passed|
|Select difficulty: Randomised words should be relevant to the difficulty selected.|Passed|
|Play again: This should prompt the user at the end of the round and restart the game if "y" is selected and exit if "n".|Passed|
|Rules to display: Should display the rules if the users input is correct. No other input is accepted and prompts the user to type either 'y' or 'n'|Passed|
|Select difficulty: Should only allow the user to input either, easy, medium, hard, error message if neither of these are selected|Passed|
|Already guessed letters: A message should display to the user that they have already guessed that specific letter|Passed|
|Win / Lose message: A message should display to the user if they have either won or lost the game|Passed|

### Fixed bugs

|What was tested / Expected results|Actual Results|What was done to fix the bug|
|---|---|---|
|Select difficulty: To display the correct word list|No word list was selected|I added the difficulty level function to the hangman function and assigned it to a variable|
|Hangmans stages: They should display in order, top to bottom|They were displaying the opposite way around|By changing the max attempts to 0|
|Hidden word: Supposed to update with the correct letters guessed|No update was displayed|Created a new function which would run this process as it was in a function shared with the stage display and guessed letters|

## Deployment

### [Heroku](https://heroku.com/apps) deployment

1. Login to Heroku
2. On the Heroku dashboard click on 'New'
3. Select 'Create New App'
4. Add an app name and select your region
5. Click 'Create App'
6. On the next page at the top click 'Settings' then 'Config Vars'
7. Click 'Reveal Config Vars' then add 'Port' key and value '8000' (Optional)
8. Scroll down and click 'Buildpack'
9. 'Add', 'Python' & 'Node.js' with Python being first (above) Node.js
10. At the top of the page again, click 'Deploy'
11. Click on 'Github' as your deployment method
12. Search the relevant repo and link these
13. Once linked, select 'Automatic deploys from' or 'Manual Deploy'
14. The app will now be hosted on Heroku.

### Cloning the GitHub repository

Cloning a repository will download a full copy of the data to your computer. This is useful when larger commits need to be pushed, adding or removing files and fixing merge conflicts.

1. Login to GitHub
2. Click the repository you wish to clone (Top left corner)
3. Click 'Code' which is shown above the list of files in the repository
4. Click the 'Local' tab, copy the HTTPS URL
5. Open Codeanywhere, click 'New Workspace'
6. Paste the copied URL into the space given under 'Repository URL'
7. Click 'Create' and the local clone will be created.

### Forking the GitHub repository

Forking a GitHub repository will allow you to make a copy of the repository, changes can then be made that will not affect the original repository. This is useful for proposed changes, ideas, fixes to an original repository.

1. Login to GitHub
2. Click the repository you wish to fork (Top left corner)
3. Click the 'Fork' drop-down in the top right-hand corner
4. Then click 'Create a new fork' you will now have a copy to work on.

## Technologies, Libraries, Frameworks & Programs Used

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    - Python was used to structure the content of the app
- [GitHub](https://github.com/)
    - GitHub is being used to store the code for this web page
- [Codeanywhere](https://codeanywhere.com/)
    - Codeanywhere was used as the development environment for this web page
- [CI Python Linter](https://pep8ci.herokuapp.com/)
    - Used to validate the code and functions
- [Heroku](https://heroku.com/apps)
    - Used to deploy the app
- [Am I Responsive?](https://ui.dev/amiresponsive)
    - Used to for the image in the README file
- [Lucid Chart](https://www.lucidchart.com/pages/)
    - Used to display the flow/logic of the app

## Credits

- Game, rules, some text content used from:
    - [How Do You Play Hangman?](https://www.wikihow.com/Play-Hangman)
- For guidance, direction and understanding the logic of Hangman and Python, these videos and pages were used:
    - [Hangman Game using Python](https://cppsecrets.com/users/5617971101051071011161151049711410997484852494964103109971051084699111109/Hangman-Game-using-Python.php)
    - [Code Your Own HANGMAN Game in Python Quickly](https://www.youtube.com/watch?v=gJBeYcqHNCM&t=291s)
    - [How To Code Hangman In Python](https://www.youtube.com/watch?v=pFvSb7cb_Us)
    - [How to add difficulty levels](https://stackoverflow.com/questions/63151142/how-to-add-difficulty-levels-to-my-number-guessing-game)
- This page was used for guidance in adding color to the terminal:
    - [How do I print colored text to the terminal?](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal)
- This page was used for guidance in adding the type writer effect:
  - [Typing effect in Python](https://stackoverflow.com/questions/20302331/typing-effect-in-python)
- Logo FIGlet:
  - [patorjk.com](https://patorjk.com/software/taag/#p=display&h=3&v=0&f=Big&t=HANGMAN%0AYOU%20WON!%0AGAME%20OVER%0APLAY%20AGAIN)
- Slack community for guidance:
  - [Slack Community](https://app.slack.com/client/T0L30B202/C027C3PLS1W)

## Acknowledgements

Thank you to my mentor Mitko Bachvarov for his guidance, advice, support as well as my husband and fellow student Iain Jackson for his advice, motivation, troubleshooting assistance throughout the process of this project.