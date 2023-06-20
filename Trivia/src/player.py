class Player:
    def __init__(self, name) -> None:
        self.coins: int = 0
        self.name: str = name
        self.position: int = 0

    def get_name(self) -> str:
        return self.name

    def get_position(self) -> int:
        return self.position

    def get_coins(self) -> int:
        return self.coins

    def is_in_penalty_box(self) -> bool:
        return False

    def move_to(self, position: int) -> None:
        self.position = position

    def win_coin(self) -> None:
        self.coins += 1