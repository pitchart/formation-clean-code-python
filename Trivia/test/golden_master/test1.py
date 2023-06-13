#!/usr/bin/env python3

import sys
sys.path.insert(0, './')

from src.game import Game

game = Game()

game.add("Cedric")
game.roll(12)
game.wrong_answer()
game.roll(2)
game.roll(13)
game.was_correctly_answered()
game.roll(13)
