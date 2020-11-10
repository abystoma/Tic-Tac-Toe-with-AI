import random
import math
from abc import ABC, abstractmethod


class Player:
    #3.
    def __init__(self, mark, player_type):
        self.mark = mark
        self.opp_mark = "O" if mark == "X" else "X"
        self.player_type = player_type

#3a
class User(Player):
    #4a
    def move(self, fields):
        coord = self.coordinates(fields)
        fields[coord] = self.mark

    def coordinates(self, fields):
        try:
            prompt = input("Enter the coordinates:")
            coord = prompt if prompt.isalpha() else int(prompt) - 1
            if coord > 8 and coord < 0:
                print("Coordinates should be from 1 to 9!")
                return self.coordinates(fields)
            if fields[coord] in Game.mark:
                print("This cell is occupied! Choose another one!")
                return self.coordinates(fields)

            return coord
        except TypeError:
            if coord == "quit":
                Game().start()
            else:
                print("You should enter numbers!")
                return self.coordinates(fields)

#abstract sublass of 3. and superclass of 3b
class Robot(ABC, Player):
    #4b
    def move(self, fields):
        print(f'Making move level "{self.player_type.lower()}"')
        coord = self.coordinates(fields)
        fields[coord] = self.mark

    @abstractmethod
    def coordinates(self, fields):
        pass

#3b if easy version
class Easy(Robot):
    #Here, AI just marks a random position
    def coordinates(self, fields):
        coord = random.randint(0, 8)
        if fields[coord] != " ":
            return self.coordinates(fields)
        return coord

#3b if medium version
class Medium(Robot):
    def coordinates(self, fields):
        coord = self.two_row_check(fields)
        if coord == None:
            coord = self.random_coord(fields)
        return coord

    def random_coord(self, fields):
        coord = random.randint(0, 8)
        if fields[coord] != " ":
            return self.coordinates(fields)
        return coord

    def two_row_check(self, fields):
        if Game.mark[0] == self.mark:
            mark_list = Game.mark
        else:
            mark_list = Game.mark.copy()
            mark_list.reverse()

        cols = [fields[i::3] for i in range(3)]

        rows = [fields[i*3:(i+1)*3] for i in range(3)]

        main_diagonal = [fields[0], fields[4], fields[8]]
        side_diagonal = [fields[2], fields[4], fields[6]]
        """Below checks various cases below where the player is one mark away from a win
        Then Returns a coordinate based on that.""" 
        for mark in mark_list:
            for index, col in enumerate(cols):
                if col.count(mark) == 2 and col.count(' '):
                    return 3 * col.index(" ") + index
            for index, row in enumerate(rows):
                if row.count(mark) == 2 and row.count(' '):
                    return 3 * (index) + row.index(" ")

            if main_diagonal.count(mark) == 2 and main_diagonal.count(' '):
                index = main_diagonal.index(' ')
                return (3 * index) + index

            if side_diagonal.count(mark) == 2 and side_diagonal.count(' '):
                index = side_diagonal.index(' ')
                return (index + 1) * 2
        return None


class Game:

    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    command = {'user': User, 'easy': Easy, 'medium': Medium}
    mark = ['X', 'O']

    def __init__(self):
        self.fields = Game.board.copy()
        self.start()
        print(self)
        self.process()

    def __str__(self):
    #displays the board/field
        result = f"---------\n" \
            f"| {' '.join(self.fields[0:3])} |\n" \
            f"| {' '.join(self.fields[3:6])} |\n" \
            f"| {' '.join(self.fields[6:9])} |\n" \
            f"---------"
        return result

    #2. This method calls different other methods based on the command
    def start(self):
        params = input("Input command: ").split()
        if params[0] == 'exit' and len(params) == 1:
            exit()
        elif params[0] == 'start' and len(params) == 3:
        #this block starts the game
            if params[1] in Game.command and params[2] in Game.command:
                self.players = [
                #a list whose elements calls the 3. constructor(s) from different subclasses 3a, 3b
                    Game.command[params[1]]('X', params[1]),
                    Game.command[params[2]]('O', params[2])
                ]
            else:
                print("Bad parameters!")
                self.start()
        else:
            print("Bad parameters!")
            self.start()

    def process(self):
        #4. This loop controls the movement by calling 4a/4b method depending on the current player
        #And it calls 4c after each move
        while True:
            for player in self.players:
                player.move(self.fields)
                print(self)
                if self.checker():
                    return None

    def checker(self):
    #4c. as the name suggests this checks whether there is a win or a draw or not
        fields = self.fields
        result = ''
        for check in Game.mark:
        #this loop checks the winning conditions for each marks
        #It works by centreing 1 game mark at a time
            if fields[4] == check:
                if (fields[7] == fields[1] == check or
                        fields[3] == fields[5] == check or
                        fields[2] == fields[6] == check or
                        fields[0] == fields[8] == check):
                    result += check
            if fields[6] == check:
                if (fields[7] == fields[8] == check or
                        fields[0] == fields[3] == check):
                    result += check
            if fields[2] == check:
                if (fields[1] == fields[0] == check or
                        fields[5] == fields[8] == check):
                    result += check

    #If there is no win / draw '' is returned and the loop at 4 continues
        if not result and not fields.count(" "):
            print("Draw\n")
            result = "Draw"
        elif result:
            print(result, 'wins\n')
        return result

#1. This starts the program, calling the Game constructor and then the 2nd method
while True:
    session = Game()
