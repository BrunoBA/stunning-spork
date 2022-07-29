
from meu_projeto.board.Board import Board
from meu_projeto.players.strategies.ColumnStrategy import ColumnStrategy
from meu_projeto.players.strategies.LineStrategy import LineStrategy
from meu_projeto.players.strategies.MainDiagonalStrategy import MainDiagonalStrategy
from meu_projeto.players.strategies.SecondaryDiagonalStrategy import SecondaryDiagonalStrategy
from meu_projeto.players.strategies.Strategy import Strategy


def test_if_first_position_is_working():
    strategy = Strategy("O", Board())
    
    assert " OO" == strategy.get_pattern_by_position(0)

def test_if_second_position_is_working():

    strategy = Strategy("O", Board())
    
    assert "O O" == strategy.get_pattern_by_position(1)

def test_if_third_position_is_working():
    strategy = Strategy("O", Board())
    
    assert "OO " == strategy.get_pattern_by_position(2)

def test_get_pattern():
    strategy = Strategy("O", Board())
    pattern = strategy.get_pattern()

    assert pattern == [' OO', 'O O', 'OO ']

def test_get_element_by_position():
    board = Board(
        [
            ['X', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
    )
    strategy = Strategy("O", board)
    element = strategy.get_element_by_position(0, 0)

    assert element == 'X'

def test_is_present_the_first_pattern():
    board = Board()
    strategy = Strategy("O", board)
    is_present_index = strategy.is_present(" OO")

    assert 0 == is_present_index

def test_is_present_the_second_pattern():
    board = Board()
    strategy = Strategy("O", board)
    is_present_index = strategy.is_present("O O")

    assert 1 == is_present_index

def test_is_present_the_last_pattern():
    board = Board()
    strategy = Strategy("O", board)
    is_present_index = strategy.is_present("OO ")

    assert 2 == is_present_index

def test_line_find_position():
    board = Board(
        [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            ['O', ' ', 'O'],
        ]
    )
    strategy = LineStrategy("O", board)
    tuple = strategy.find_position()

    assert (2, 1) == tuple

def test_column_find_position():
    board = Board(
        [
            [' ', ' ', 'O'],
            [' ', ' ', ' '],
            [' ', ' ', 'O'],
        ]
    )
    strategy = ColumnStrategy("O", board)
    tuple = strategy.find_position()

    assert (1, 2) == tuple

def test_main_diagonal_find_position():
    board = Board(
        [
            ['O', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', 'O'],
        ]
    )
    strategy = MainDiagonalStrategy("O", board)
    tuple = strategy.find_position()

    assert (1, 1) == tuple

def test_secondary_diagonal_find_position():
    board = Board(
        [
            [' ', ' ', 'O'],
            [' ', ' ', ' '],
            ['O', ' ', ' '],
        ]
    )
    strategy = SecondaryDiagonalStrategy("O", board)
    tuple = strategy.find_position()

    assert (1, 1) == tuple