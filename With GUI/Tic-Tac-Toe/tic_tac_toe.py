import sys # For handling system operattions
import random # For generating random numbers
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout # For creating the GUI

# Class Skeleton for the TicTacToe game
class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    # Define the GUI layout and components
    def init_ui(self):
        # Main window title and size
        self.setWindowTitle('Tic-Tac-Toe')
        self.setGeometry(100, 100, 300, 350)

        self.grid_layout = QGridLayout()
        self.buttons = [[QPushButton('') for _ in range(3)] for _ in range(3)]

        # Create the 3x3 grid of buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setFixedSize(80, 80)
                self.buttons[i][j].clicked.connect(lambda _, row=i, col=j: self.play_turn(row, col))
                self.grid_layout.addWidget(self.buttons[i][j], i, j)
            
        self.status_label = QLabel('Player X\'s turn') # Display current player's turn
        self.reset_button = QPushButton('Reset Game') # Button to reset the game
        self.reset_button.clicked.connect(self.reset_game)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.status_label)
        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addWidget(self.reset_button)

        self.setLayout(self.v_layout)

        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X' if random.randint(0, 1) == 1 else 'O'
        self.update_status() # Sets the initial player turn automatically

    # Define the game logic
    def play_turn(self, row, col):
        # Check if the clicked button is empty and if the game is still ongoing
        if self.board[row][col] == '' and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].setText(self.current_player)

            # Check for a winner or a draw
            if self.check_winner():
                self.status_label.setText(f'Player {self.current_player} Wins!')
            elif self.is_board_full():
                self.status_label.setText('It\'s a Draw!')
            else:
                # Switch players if game is still ongoing

                self.current_player = 'X' if self.current_player == 'O' else 'O'
                self.update_status()

    # Verifies if a player has won by checking rows, columns, and diagonals for a win
    def check_winner(self):
        for row in self.board:
            if row.count(row[0]) == 3 and row[0] != '':
                return True
            
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != '':
                return True
            
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '':
            return True
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '':
            return True
        
        return False

    # Check if the board is full (draw condition)
    def is_board_full(self):
        return all(self.board[i][j] != '' for i in range(3) for j in range(3)) #returns True if all cells are filled

    # Update the status label to show the current player's turn
    def update_status(self):
        self.status_label.setText(f'Player {self.current_player}\'s Turn')
    
    # Reset the game to its initial state
    def reset_game(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText('')
        self.current_player = 'X' if random.randint(0, 1) == 1 else 'O'
        self.update_status()

if __name__ == '__main__':
    app = QApplication(sys.argv) # Create an instance of QApplication
    window = TicTacToe() # Create an instance of TicTacToe
    window.show() # Show the game window
    sys.exit(app.exec_()) # Exit the application when the game is closed


'''
Yay friend! You seriously just built a whole Tic-Tac-Toe game using Python and PyQt5 — how cool is that?!

You nailed some awesome stuff like:
- Setting up the board with PyQt5 layouts
- Making the buttons actually *do* things when clicked
- Keeping everything organized with classes (like a pro!)

Wanna take it even further? Here’s what you could try next:
- Add a little AI so you can play solo
- Make it super cute with custom colors and styles
- Keep track of wins so y’all can get competitive!

I'm so proud of you — keep going, you're doing amazing! 💻🎉
'''