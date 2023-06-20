from src.player import Player


def test_create_player():
    player = Player('Maxime')
    assert player.get_name() == 'Maxime'
    assert player.get_position() == 0
    assert player.get_coins() == 0
    assert player.is_in_penalty_box() == False

def test_move_player():
    player = Player('Paul')
    player.move_to(9)
    assert player.get_position() == 9
