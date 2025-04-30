import random # For computer to make a random selection
import os # To clear the screen between rounds
import re # To validate the user input

def check_play_status():
    # Must be a valid response
    valid_responses = ['yes', 'no', 'y']
    while True:
        try:
            response = input('Do you wish to play again? (Yes or No): ')
            if response.lower() not in valid_responses:
                raise ValueError('Yes or No only')

            # Game continues if 'yes' or 'y'
            if response.lower() in ['yes', 'y']:
                return True
            # If 'no' clear the screen, display message and exit
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Thanks for playing!')
                exit()
        
        # Repeats the question until a valid response is given
        except ValueError as err:
            print(err)

def play_rps():
    user_score = 0
    computer_score = 0
    play = True

    # Game runs until the user decides to stop
    while play:
        # The screen clears at the beginning of each round
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\nRock, Paper, Scissors - Shoot!')

        user_choice = input('Choose your weapon [R]ock, [P]aper, or [S]cissors: ')

        # Validate input using regex
        if not re.match("^[RrPpSs]$", user_choice):
            print('Invalid choice! Try again.')
            continue

        # How the user chooses rock, paper or scrissors
        print(f'You chose: {user_choice.upper()}')
        choices = ['R', 'P', 'S']
        # How the computer chooses, rock, paper or scissors
        opp_choice = random.choice(choices)
        print(f'I chose: {opp_choice}')

        # Determine the winner
        if opp_choice == user_choice.upper():
            print('It\'s a Tie!')
        elif (opp_choice == 'R' and user_choice.upper() == 'S') or \
             (opp_choice == 'S' and user_choice.upper() == 'P') or \
             (opp_choice == 'P' and user_choice.upper() == 'R'):
            print(f'{opp_choice} beats {user_choice.upper()}, I win!')
            computer_score += 1
        else:
            print(f'{user_choice.upper()} beats {opp_choice}, You win!')
            user_score += 1

        print(f'Score - You: {user_score}, Computer: {computer_score}')
        # Goes back to the first function and ask if they want to play again
        play = check_play_status()

if __name__ == '__main__':
    play_rps()

'''
Rock Paper Scissors Game Notes

Main Game Function: play_rps()
-------------------------------
- Gets input from the user and checks if it's valid ("R", "P", or "S").
- Uses the random module to let the computer make a choice.
- Compares the player's and computer's choices using if-elif-else statements to decide the winner.

Why Use a while Loop?
---------------------
- Keeps the game running in a loop until the player decides to quit.
- Resets game variables each round, allowing fresh starts.
- Enhances interactivity and user experience.

Exiting the Game
----------------
- When the user wants to quit, set play = False to break the loop.

Clearing the Screen
-------------------
- Keeps the screen clean between rounds to avoid clutter.
- Use 'cls' for Windows and 'clear' for Linux/macOS.
- Use os.name to check the operating system and run the correct command.

Validating Input with re.match()
--------------------------------
- Makes sure the user only enters valid characters: "R", "P", or "S".
- Uses regex to check if the input is one of the allowed single characters.
- If input is invalid, show an error and ask again.

Using random.choice()
---------------------
- Randomly picks between Rock, Paper, and Scissors for the computer.
- Keeps the game fair and unpredictable.
- Makes the code shorter and cleaner by picking from a list.

The __name__ == "__main__" Check
--------------------------------
- When the script is run directly, __name__ is "__main__" and play_rps() runs.
- When the script is imported into another file, __name__ is set to the file name, and play_rps() won’t run automatically.

Why This Is Best Practice
-------------------------
- Makes sure the game only runs when it should.
- Prevents the code from running if imported elsewhere.
- Helps keep the code modular and reusable for future projects.
'''
