from meu_projeto.board.Board import Board


board = Board([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', 'X']])

print(board.get_positions_available())

copy_board = Board(board.get_matrix())
copy_board.set_position('O', 1, 1)

print(copy_board)

copy_board.roll_back_move()

print(copy_board)
