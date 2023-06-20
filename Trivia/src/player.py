class Player:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name

    def get_position(self):
        return 0

    def get_coins(self):
        return 0

    def is_in_penalty_box(self):
        return False