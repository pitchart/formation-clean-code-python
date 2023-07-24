#!/usr/bin/env python3
from enum import Enum


class Category(Enum):
    def __str__(self):
        return str(self.value)

    POP = 'Pop'
    SCIENCE = 'Science'
    SPORTS = 'Sports'
    ROCK = 'Rock'

    @staticmethod
    def build_dict_categories():
        return {0: Category.POP, 1: Category.SCIENCE, 2: Category.SPORTS, 3: Category.ROCK}


class Game:
    def __init__(self):
        self.MIN_NB_PLAYERS = 2
        self.MAX_NB_PLAYERS = 6
        self.BOARD_SIZE = 12

        self.players = []
        self.places = [0] * self.MAX_NB_PLAYERS
        self.purses = [0] * self.MAX_NB_PLAYERS
        self.in_penalty_box = [0] * self.MAX_NB_PLAYERS

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        self.questions_dict = {
            Category.POP: [],
            Category.SCIENCE: [],
            Category.SPORTS: [],
            Category.ROCK: []
        }

        for i in range(50):
            self.questions_dict[Category.POP].append("Pop Question %s" % i)
            self.questions_dict[Category.SCIENCE].append("Science Question %s" % i)
            self.questions_dict[Category.SPORTS].append("Sports Question %s" % i)
            self.questions_dict[Category.ROCK].append("Rock Question %s" % i)

    def is_playable(self):
        return self.how_many_players >= self.MIN_NB_PLAYERS

    def add(self, player_name):
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

    def roll(self, roll):
        print("%s is the current player" % self.players[self.current_player])
        print("They have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print("%s is getting out of the penalty box" % self.players[self.current_player])
                self._move_player_on_board(roll)
                self._ask_question()
            else:
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
                self.is_getting_out_of_penalty_box = False
        else:
            self._move_player_on_board(roll)
            self._ask_question()

    def _move_player_on_board(self, roll):
        self.places[self.current_player] = self.places[self.current_player] + roll
        if self.places[self.current_player] >= self.BOARD_SIZE:
            self.places[self.current_player] = self.places[self.current_player] - self.BOARD_SIZE
        print(self.players[self.current_player] + \
              '\'s new location is ' + \
              str(self.places[self.current_player]))
        print("The category is %s" % self._current_category)

    def _ask_question(self):
        print(self.questions_dict[self._current_category].pop(0))


    @property
    def _current_category(self):
        choice = self.places[self.current_player]%len(Category)
        categories = Category.build_dict_categories()
        return categories[choice]

    def was_correctly_answered(self):
        winner = True
        if (self.in_penalty_box[self.current_player] and self.is_getting_out_of_penalty_box) or not self.in_penalty_box[self.current_player]:
                print('Answer was correct!!!!')
                self.purses[self.current_player] += 1
                print(self.players[self.current_player] + \
                      ' now has ' + \
                      str(self.purses[self.current_player]) + \
                      ' Gold Coins.')
                winner = self._did_player_win()

        self.next_player()
        return winner

    def next_player(self):
        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self.next_player()
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)
