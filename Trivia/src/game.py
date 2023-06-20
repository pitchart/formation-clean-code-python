#!/usr/bin/env python3
from typing import Dict, List
from strenum import StrEnum

from src.player import Player

MIN_PLAYERS = 2
BOARD_SIZE = 12
MAX_PLAYERS = 6


class Category(StrEnum):
    POP = 'Pop'
    SPORTS = 'Sports'
    SCIENCE = 'Science'
    ROCK = 'Rock'


class Game:
    def __init__(self):
        self.players = []
        self.players_list =[]
        self.places = [0] * MAX_PLAYERS
        self.purses = [0] * MAX_PLAYERS
        self.in_penalty_box = [0] * MAX_PLAYERS

        self.categories: Dict[int, Category] = {
            0: Category.POP,
            1: Category.SCIENCE,
            2: Category.SPORTS,
            3: Category.ROCK
        }
        self.questions: Dict[Category, List[str]] = {
            category : [f"{category} Question {i}" for i in range(50)] 
            for category 
            in self.categories.values()
        }
        
        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

    def is_playable(self):
        return self.how_many_players >= MIN_PLAYERS
    
    def add_player(self, player_name):
        self.players_list.append(Player(player_name))
        self.players.append(player_name)
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False

        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    @staticmethod
    def _is_roll_even(roll: int):
        return roll % 2 != 0

    def roll(self, roll):
        print("%s is the current player" % self.players_list[self.current_player].get_name())
        print("They have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player] and not self._is_roll_even(roll):
            print("%s is not getting out of the penalty box" % self.players_list[self.current_player].get_name())
            self.is_getting_out_of_penalty_box = False
            return

        if self.in_penalty_box[self.current_player]:
            self.is_getting_out_of_penalty_box = True
            print("%s is getting out of the penalty box" % self.players_list[self.current_player].get_name())

        self._move_player(roll)
        print(self.players_list[self.current_player].get_name() + \
              '\'s new location is ' + \
              str(self.places[self.current_player]))
        print("The category is %s" % str(self._current_category))
        self._ask_question()

    def _move_player(self, roll):
        self.places[self.current_player] = (self.places[self.current_player] + roll) % BOARD_SIZE

    def _ask_question(self):
        print(self.questions[self._current_category].pop(0))

    @property
    def _current_category(self):
        category_id = self.places[self.current_player] % len(Category)
        return self.categories[category_id]

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                print('Answer was correct!!!!')
                self.win_coin()
                print(self.players_list[self.current_player].get_name() + \
                      ' now has ' + \
                      str(self.purses[self.current_player]) + \
                      ' Gold Coins.')

                winner = self._did_player_win()

                self.next_player()
                return winner
            else:
                winner = True
                self.next_player()
                return winner

        print("Answer was corrent!!!!")
        self.win_coin()
        print(self.players_list[self.current_player].get_name() + \
              ' now has ' + \
              str(self.purses[self.current_player]) + \
              ' Gold Coins.')

        winner = self._did_player_win()

        self.next_player()
        return winner

    def next_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def win_coin(self):
        self.purses[self.current_player] += 1

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players_list[self.current_player].get_name() + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self.next_player()
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)
