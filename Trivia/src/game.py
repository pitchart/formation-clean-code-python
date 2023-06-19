#!/usr/bin/env python3
from typing import Dict, List
from strenum import StrEnum

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
        self.places = [0] * MAX_PLAYERS
        self.purses = [0] * MAX_PLAYERS
        self.in_penalty_box = [0] * MAX_PLAYERS

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.questions: Dict[Category, List[str]] = {
            Category.POP: self.pop_questions,
            Category.SCIENCE: self.science_questions,
            Category.SPORTS: self.sports_questions,
            Category.ROCK: self.rock_questions,
        }

        self.categories: Dict[int, Category] = {
            0: Category.POP,
            1: Category.SCIENCE,
            2: Category.SPORTS,
            3: Category.ROCK
        }

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(50):

            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)

    def is_playable(self):
        return self.how_many_players >= MIN_PLAYERS

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
                self.places[self.current_player] = self.places[self.current_player] + roll
                if self.places[self.current_player] >= BOARD_SIZE:
                    self.places[self.current_player] = self.places[self.current_player] - BOARD_SIZE

                print(self.players[self.current_player] + \
                      '\'s new location is ' + \
                      str(self.places[self.current_player]))
                print("The category is %s" % str(self._current_category))
                self._ask_question()
            else:
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
                self.is_getting_out_of_penalty_box = False
        else:
            self.places[self.current_player] = self.places[self.current_player] + roll
            if self.places[self.current_player] >= BOARD_SIZE:
                self.places[self.current_player] = self.places[self.current_player] - BOARD_SIZE

            print(self.players[self.current_player] + \
                  '\'s new location is ' + \
                  str(self.places[self.current_player]))
            print("The category is %s" % str(self._current_category))
            self._ask_question()

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
                self.purses[self.current_player] += 1
                print(self.players[self.current_player] + \
                      ' now has ' + \
                      str(self.purses[self.current_player]) + \
                      ' Gold Coins.')

                winner = self._did_player_win()
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0

                return winner
            else:
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0
                return True



        else:

            print("Answer was corrent!!!!")
            self.purses[self.current_player] += 1
            print(self.players[self.current_player] + \
                  ' now has ' + \
                  str(self.purses[self.current_player]) + \
                  ' Gold Coins.')

            winner = self._did_player_win()
            self.current_player += 1
            if self.current_player == len(self.players): self.current_player = 0

            return winner

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)
