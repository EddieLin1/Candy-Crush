import candymod as game
board = []
points = 0
turns = 0
for i in range(9):
    board.append([])
    for j in range(7):
        board[i].append(0)
int_board = game.make_initial_board(board)
fin_board = game.check_initial_board(int_board)
game.draw_board(fin_board)

game_unfinished = True
while game_unfinished and turns < 20:
    game.show_turns(turns)
    game.show_points(points)

    pos1 = game.click()
    conv1 = game.convert_positions1(pos1)
    game.select(conv1, 0)
    pos2 = game.click()
    conv2 = game.convert_positions1(pos2)
    game.select(conv2, 1)
    pos = [pos1, pos2]
    converted_positions = game.convert_positions(pos)
    turns += 1
    game.draw_board(board)
    if game.check_if_adjacent(converted_positions):
        board = game.switch(converted_positions, board)
        game.draw_board(board)
        one_turn = game.check_combo(board)
        if game.check_combo(board):
            while one_turn:
                board = game.clear_combo(board)
                game.draw_board(board)
                board = game.collapse(board)
                game.draw_board(board[0])
                points += board[1]
                board = game.repopulate(board[0])
                game.draw_board(board)
                one_turn = game.check_combo(board)
        else:
            game.switch(converted_positions, board)
            game.draw_board(board)
    else:
        game.draw_board(board)
        game_unfinished = True


while True:
    game.show_points(points)
    game.show_turns(turns)
    game.show_end()