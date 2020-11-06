import random


class TicTacToe:

    board = {1: " ", 2: " ", 3: " ",
             4: " ", 5: " ", 6: " ",
             7: " ", 8: " ", 9: " "}

    coordinate_conversion = {(1, 3): 1, (2, 3): 2, (3, 3): 3,
                             (1, 2): 4, (2, 2): 5, (3, 2): 6,
                             (1, 1): 7, (2, 1): 8, (3, 1): 9}

    def __init__(self):
        pass

    def menu(self):
        while True:
            var = input("Input command: ")

            if var == "exit":
                exit()
            if len(var.split()) != 3:
                print("Bad parameters!")
                continue

            else:
                if var.split()[2] == "easy" and var.split()[1] == "easy":
                    self.print_board()
                    while True:
                        self.moves_1()
                elif var.split()[1] == "user" and var.split()[2] == "easy" or var.split()[2] == "user" and var.split()[1] == "easy":
                    self.print_board()

                    while True:
                        self.coordinates()
                elif var.split()[1] == "user" and var.split()[2] == "user":
                    self.print_board()

                    while True:
                        self.moves_2()

    def check(self):
        try:
            x, y = [int(i) for i in input("Enter the coordinates:").split(" ")]

            # if x not in range(1, 4) or y not in range(1, 4):
            #   print("Coordinates should be from 1 to 3!")
            index = TicTacToe.coordinate_conversion[x, y]
            # print(index)
        except:
            print("You should enter numbers!")

        if x not in range(1, 4) or y not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
            return None

        if TicTacToe.board[index] != " ":
            print("This cell is occupied! Choose another one!")
            return None
        return TicTacToe.coordinate_conversion[x, y]

    def moves_2(self):
        while True:
            self.move_user_1(self.check())
            if self.board_state():
                print(self.board_state())
                self.menu()
            self.move_user_2(self.check())
            if self.board_state():
                print(self.board_state())
                self.menu()

    def moves_1(self):
        self.move_AI_1()
        if self.board_state():
            print(self.board_state())
            self.menu()
        self.move_AI_2()
        if self.board_state():
            print(self.board_state())
            self.menu()

    def print_board(self):
        print("---------")
        print('| ' + TicTacToe.board[1] + ' ' +
              TicTacToe.board[2] + ' ' + TicTacToe.board[3] + ' |')
        print('| ' + TicTacToe.board[4] + ' ' +
              TicTacToe.board[5] + ' ' + TicTacToe.board[6] + ' |')
        print('| ' + TicTacToe.board[7] + ' ' +
              TicTacToe.board[8] + ' ' + TicTacToe.board[9] + ' |')
        print("---------")

    def coordinates(self):

        try:
            x, y = [int(i) for i in input("Enter the coordinates:").split(" ")]

            # if x not in range(1, 4) or y not in range(1, 4):
            #   print("Coordinates should be from 1 to 3!")
            index = TicTacToe.coordinate_conversion[x, y]
            # print(index)
        except:
            print("You should enter numbers!")

        if x not in range(1, 4) or y not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
            return None

        if TicTacToe.board[index] != " ":
            print("This cell is occupied! Choose another one!")
            return None
        ind = TicTacToe.coordinate_conversion[x, y]
        self.move_user_1(ind)
        if self.board_state():
            print(self.board_state())
            self.menu()
        self.move_AI_2()
        if self.board_state():
            print(self.board_state())
            self.menu()

    def move_user_1(self, index):
        # print(index)
        TicTacToe.board[index] = "X"
        self.print_board()

    def move_user_2(self, index):
        # print(index)
        TicTacToe.board[index] = "O"
        self.print_board()

    def move_AI_1(self):
        print('Making move level "easy"')
        while True:
            index = TicTacToe.coordinate_conversion[random.randint(
                1, 3), random.randint(1, 3)]
            if TicTacToe.board[index] == " ":
                TicTacToe.board[index] = "X"
                break
        self.print_board()

    def move_AI_2(self):
        print('Making move level "easy"')
        while True:
            index = TicTacToe.coordinate_conversion[random.randint(
                1, 3), random.randint(1, 3)]
            if TicTacToe.board[index] == " ":
                TicTacToe.board[index] = "O"
                break
        self.print_board()

    def board_wins(self, board, symbol):
        # 3 horizontal checks for wins
        if board[1] == board[2] == board[3] == symbol:
            return True
        elif board[4] == board[5] == board[6] == symbol:
            return True
        elif board[7] == board[8] == board[9] == symbol:
            return True

        # 3 vertical checks for wins
        elif board[1] == board[4] == board[7] == symbol:
            return True
        elif board[2] == board[5] == board[8] == symbol:
            return True
        elif board[3] == board[6] == board[9] == symbol:
            return True

        # 2 diagonal checks for wins
        elif board[1] == board[5] == board[9] == symbol:
            return True
        elif board[3] == board[5] == board[7] == symbol:
            return True

        else:
            return False

    def board_state(self):
        if self.board_wins(TicTacToe.board, "X"):
            return "X wins"
        elif self.board_wins(TicTacToe.board, "O"):
            return "O wins"

        elif list(TicTacToe.board.values()).count(" ") == 0:
            return "Draw"


Game = TicTacToe()
while True:
    Game.menu()
