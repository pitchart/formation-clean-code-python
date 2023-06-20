class Player:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        pass

    def get_position(self):
        pass

    def get_coins(self):
        pass

    def is_in_penalty_box(self):
        pass


def test_create_player():
    player = Player('Maxime')
    assert player.get_name() == 'Maxime'
    assert player.get_position() == 0
    assert player.get_coins() == 0
    assert player.is_in_penalty_box() == False