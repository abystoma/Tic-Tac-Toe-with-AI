import random
from abc import ABC, abstractmethod


class Player:
    def __init__(self, mark, opp_mark):
        self.mark = mark
        self.opp_mark = opp_mark


class User(Player):
    def move(self, field):
        coord = self.coordinates(field)
        field[coord] = self.mark
        return field

    def coordinates(self, field):
        try:
            x, y = [int(i) for i in input("Enter the coordinates:").split(" ")]
            index = Game.coordinate_conversion[x, y]
        except:
            print("You should enter numbers!")
            return self.coordinates(field)

        if x not in range(1, 4) or y not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
            return self.coordinates(field)

        if field[index] in Game.mark:
            print("This cell is occupied! Choose another one!")
            return self.coordinates(field)

        index = Game.coordinate_conversion[x, y]
        return index


class Robot(ABC, Player):
    def move(self, field):
        print(f'Making move level "{self.__class__.__name__.lower()}"')
        coords_1 = self.coordinates(field)
        field[coords_1] = self.mark
        return field

    @abstractmethod
    def coordinates(self, field):
        pass


class Easy(Robot):
    def coordinates(self, field):
        coords = Game.coordinate_conversion[random.randint(
            1, 3), random.randint(1, 3)]
        if field[coords] != " ":
            return self.coordinates(field)
        return coords


class Game:

    board = {1: " ", 2: " ", 3: " ",
             4: " ", 5: " ", 6: " ",
             7: " ", 8: " ", 9: " "}

    coordinate_conversion = {(1, 3): 1, (2, 3): 2, (3, 3): 3,
                             (1, 2): 4, (2, 2): 5, (3, 2): 6,
                             (1, 1): 7, (2, 1): 8, (3, 1): 9}

    command = {'user': User, 'easy': Easy, 'start': None, 'exit': exit}
    mark = ['X', 'O']

    def __init__(self):
        self.field = Game.board.copy()
        self.start()
        print(self)
        self.process()

    def __str__(self):
        result = f"---------\n" \
                 f"| {self.field[1]} {self.field[2]} {self.field[3]} |\n" \
                 f"| {self.field[4]} {self.field[5]} {self.field[6]} |\n" \
                 f"| {self.field[7]} {self.field[8]} {self.field[9]} |\n" \
                 f"---------"
        return result

    def start(self):
        params = input("Input command: ").split()
        if params[0] == 'exit' and len(params) == 1:
            exit()
        elif params[0] == 'start' and len(params) == 3:
            if params[1] in Game.command and params[2] in Game.command:
                self.first = Game.command[params[1]]('X', 'O')
                self.second = Game.command[params[2]]('O', 'X')
        else:
            print("Bad parameters!")
            self.start()

    def process(self):
        while True:
            for player in [self.first, self.second]:
                self.field = player.move(self.field)
                print(self)
                if Game.checker(self.field):
                    return None

    @staticmethod
    def checker(field):
        result = ''
        for check in Game.mark:
            if field[5] == check:
                if (field[8] == field[2] == check or
                        field[4] == field[6] == check or
                        field[3] == field[7] == check or
                        field[1] == field[9] == check):
                    result += check
            if field[7] == check:
                if (field[8] == field[9] == check or
                        field[1] == field[4] == check):
                    result += check
            if field[3] == check:
                if (field[2] == field[1] == check or
                        field[6] == field[9] == check):
                    result += check

        if not result and not list(field.values()).count(" "):
            print("Draw\n")
            result = "Draw"
        elif result:
            print(result, 'wins\n')
        return result


while True:
    session = Game()
