#!/usr/bin/env python3

import sys
sys.path.insert(0, './')

from src.game import Game

game = Game()

game.add_player("Cedric");
game.add_player("Eloise");
game.roll(1);
game.wrong_answer();
game.roll(2);
game.was_correctly_answered();
game.roll(2);
game.was_correctly_answered();
game.roll(2);
game.was_correctly_answered();
game.roll(2);
game.was_correctly_answered();
game.roll(2);
game.was_correctly_answered();
game.roll(2);
game.was_correctly_answered();
game.roll(2);
game.was_correctly_answered();
game.roll(2);
game.was_correctly_answered();
game.roll(2);
game.was_correctly_answered();