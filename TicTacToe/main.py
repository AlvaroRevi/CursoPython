class TicTacToe:
    def __init__(self):
        # Initialize the game board as a 3x3 grid
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def display_board(self):
        """Display the current state of the board"""
        print("\n   0   1   2")
        for i in range(3):
            print(f"{i}  {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]}")
            if i < 2:
                print("  -----------")
        print()

    def display_instructions(self):
        """Display game instructions"""
        print("Welcome to Tic Tac Toe!")
        print("Players will take turns placing X's and O's on the board.")
        print("Enter your move as row,col (e.g., 0,1 for top middle)")
        print("Rows and columns are numbered 0-2")

    def make_move(self, row, col):
        """Make a move on the board"""
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            return True
        return False

    def is_valid_move(self, row, col):
        """Check if the move is valid"""
        if 0 <= row <= 2 and 0 <= col <= 2:
            return self.board[row][col] == ' '
        return False

    def check_winner(self):
        """Check if there's a winner"""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def is_board_full(self):
        """Check if the board is full"""
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def switch_player(self):
        """Switch between players"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_player_move(self):
        """Get player input for their move"""
        while True:
            try:
                move = input(f"Player {self.current_player}, enter your move (row,col): ")
                row, col = map(int, move.split(','))
                return row, col
            except ValueError:
                print("Invalid input! Please enter row,col (e.g., 0,1)")
            except:
                print("Invalid input! Please enter row,col (e.g., 0,1)")

    def play(self):
        """Main game loop"""
        self.display_instructions()

        while True:
            self.display_board()

            # Get player move
            row, col = self.get_player_move()

            # Try to make the move
            if self.make_move(row, col):
                # Check for winner
                winner = self.check_winner()
                if winner:
                    self.display_board()
                    print(f"🎉 Player {winner} wins!")
                    break

                # Check for tie
                if self.is_board_full():
                    self.display_board()
                    print("It's a tie! Good game!")
                    break

                # Switch players
                self.switch_player()
            else:
                print("Invalid move! That position is already taken or out of bounds.")

        # Ask if players want to play again
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again == 'y' or play_again == 'yes':
            self.__init__()  # Reset the game
            self.play()
        else:
            print("Thanks for playing Tic Tac Toe!")


def main():
    """Start the game"""
    game = TicTacToe()
    game.play()


if __name__ == "__main__":
    main()