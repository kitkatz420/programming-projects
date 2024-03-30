import math
import random


class Player:
    def _init_(self, letter):
        #letter is x or o
        self.letter=letter

    #we want all players to get their next move
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def _init_(self, letter):
        super()._init_(letter)


    def get_move(self, game):
        square=random.choice[game.available_moves()]
        return square


class HumanPlayer(Player):
    def _init_(self, letter):
        super()._init_(letter)


    def get_move(self, game):
        valid_square=False
        val= None
        while not valid_square:
            square=input(self.letter+'\'s turn. Input move (0-9):')
            #we're going to check that this is a correct value by trying to cast
            #it to an integer, and if it's not, then we say its invalid
            #if that spot not available on the board, we also say its invalid
            try:
                val=int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square=True#if thes are succesful, then yay!
            except ValueError:
                print('Invalid Try Again')

        return val
