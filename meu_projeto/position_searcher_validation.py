from meu_projeto.board.Board import Board
from meu_projeto.players.strategies.PositionSearcher import PositionSearcher


board = Board()

board.set_position('X', 1, 1)
board.set_position('O', 1, 2)
# board.set_position("X", 1,3)
# board.set_position("O", 2,1)
# board.set_position("X", 2,2)
# board.set_position("O", 2,3)

# board.set_position("X", 3,2)
# board.set_position("O", 3,1)


print(board)

position_searcher = PositionSearcher()
pos = position_searcher.find_position(board, 'X', 'X')

print(pos.get_move())
(line, col) = pos.get_move()
board.set_position(
    'X',
    line + 1,
    col + 1,
)


print(board)
