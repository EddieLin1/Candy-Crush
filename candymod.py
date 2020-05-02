import random
import stddraw
import picture

a = 0
stddraw.setCanvasSize(600, 850)
stddraw.setXscale(0, 7)
stddraw.setYscale(-1, 9)
for i in range(8):
    stddraw.line(0, 1 + i, 8, 1 + i)
for j in range(10):
    stddraw.line(1 + j, 0, 1 + j, 10)


# make initial master array with all the values of shapes
def make_initial_board(board_1):
    for i in range(9):
        for j in range(7):
            num = random.randint(1, 7)
            board_1[i][j] = num
    return board_1


# check initial board, return matrix
def check_initial_board(board):
    for i in range(9):
        for j in range(7):
            if (j + 2) < 7 and board[i][j] == board[i][j+1] and board[i][j+1] == board[i][j+2]:
                if board[i][j] <= 3:
                    board[i][j+1] = random.randint(4,7)
                if board[i][j] >= 4:
                    board[i][j+1] = random.randint(1,3)
            if (i + 2) < 9 and board[i][j] == board[i+1][j] and board[i+1][j] == board[i+2][j]:
                if board[i][j] <= 3:
                    board[i+1][j] = random.randint(4, 7)
                if board[i][j] >= 4:
                    board[i+1][j] = random.randint(1, 3)
    return board


# draw_board, take in martrix draw board
def candy1(x,y):
    stddraw.picture(picture.Picture('candy1.png'), x, y)


def candy2(x,y):
    stddraw.picture(picture.Picture('candy2.png'), x, y)


def candy3(x,y):
    stddraw.picture(picture.Picture('candy3.png'), x, y)


def candy4(x,y):
    stddraw.picture(picture.Picture('candy4.png'), x, y)


def candy5(x,y):
    stddraw.picture(picture.Picture('candy5.png'), x, y)


def candy6(x,y):
    stddraw.picture(picture.Picture('candy6.png'), x, y)


def candy7(x,y):
    stddraw.picture(picture.Picture('candy7.png'), x, y)


def draw_board(board):
    stddraw.clear()
    x_axis = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
    y_axis = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
    for i in range(9):
        for j in range(7):
            if board[i][j] == 0:
                stddraw.setFontSize(100)
                stddraw.text(x_axis[j], y_axis[i], ' ')
            if board[i][j] == 1:
                candy1(x_axis[j], y_axis[i])
            if board[i][j] == 2:
                candy2(x_axis[j], y_axis[i])
            if board[i][j] == 3:
                candy3(x_axis[j], y_axis[i])
            if board[i][j] == 4:
                candy4(x_axis[j], y_axis[i])
            if board[i][j] == 5:
                candy5(x_axis[j], y_axis[i])
            if board[i][j] == 6:
                candy6(x_axis[j], y_axis[i])
            if board[i][j] == 7:
                candy7(x_axis[j], y_axis[i])
    stddraw.show(10)


def switch(converted_positions, board):
    switch_array = []
    switch_array.append(board[converted_positions[0][1]][converted_positions[0][0]])
    switch_array.append(board[converted_positions[1][1]][converted_positions[1][0]])
    board[converted_positions[0][1]][converted_positions[0][0]] = switch_array[1]
    board[converted_positions[1][1]][converted_positions[1][0]] = switch_array[0]
    return board


def click():
    while True:
        stddraw.show(0)
        if stddraw.mousePressed():
            mx1 = stddraw.mouseX()
            my1 = stddraw.mouseY()
            return [mx1, my1]


def convert_positions1(pos):
    conv_pos = []
    for i in range(8):
        if i <= pos[0] <= (i+1):
            conv_pos.append(i)
    for j in range(10):
        if j <= pos[1] <= (j+1):
            conv_pos.append(j)
    return conv_pos


def convert_positions(position_1):
    conv_pos_1 = [[], []]
    x_axis = [0, 1, 2, 3, 4, 5, 6, 7]
    y_axis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(2):
        for j in range(len(x_axis)):
            if x_axis[j] <= position_1[i][0] < x_axis[j + 1]:
                conv_pos_1[i].append(x_axis[j])
    for i in range(2):
        for j in range(len(y_axis)):
            if y_axis[j] <= position_1[i][1] < y_axis[j + 1]:
                conv_pos_1[i].append(y_axis[j])
    return conv_pos_1


def select(array, col):
    if col == 0:
        stddraw.setPenColor(stddraw.BLUE)
        stddraw.setPenRadius(0.03)
        stddraw.line(array[0], array[1], array[0] + 1, array[1])
        stddraw.line(array[0] + 1, array[1], array[0] + 1, array[1] + 1)
        stddraw.line(array[0] + 1, array[1] + 1, array[0], array[1] + 1)
        stddraw.line(array[0], array[1] + 1, array[0], array[1])
        stddraw.show(0)
    else:
        stddraw.setPenColor(stddraw.RED)
        stddraw.setPenRadius(0.03)
        stddraw.line(array[0], array[1], array[0] + 1, array[1])
        stddraw.line(array[0] + 1, array[1], array[0] + 1, array[1] + 1)
        stddraw.line(array[0] + 1, array[1] + 1, array[0], array[1] + 1)
        stddraw.line(array[0], array[1] + 1, array[0], array[1])
        stddraw.show(0)


def check_if_adjacent(positions_1):
    x = positions_1[0][0]
    y = positions_1[0][1]
    correct = []
    counter1 = -1
    for i in range(2):
        correct.append([x, y + counter1])
        counter1 = 1
    counter2 = -1
    for i in range(2):
        correct.append([x + counter2, y])
        counter2 = 1
    if positions_1[1] in correct:
        return True
    else:
        return False


def check_combo(board):
    for i in range(9):
        for j in range(7):
            for k in range(5):
                if board[i][k] == board[i][k+1] == board[i][k+2] == j+1:
                    return True
    for i in range(7):
        for j in range(7):
            for k in range(7):
                if board[i][k] == board[i + 1][k] == board[i + 2][k] == j+1:
                    return True
    return False


def clear_combo(board):
    indices = []
    for i in range(9):
        for j in range(7):
            if (j + 2) < 7 and board[i][j] == board[i][j+1] and board[i][j+1] == board[i][j+2]:
                for k in range(3):
                    indices.append([i, j+k])
            if (i + 2) < 9 and board[i][j] == board[i+1][j] and board[i+1][j] == board[i+2][j]:
                for k in range(3):
                    indices.append([i+k, j])
    for i in range(len(indices)):
        board[indices[i][0]][indices[i][1]] = 0
    return board


def collapse(board):
    points = 0
    for col in range(7):
        counter = 0
        for row in range(9):
            if board[row][col] == 0:
                counter += 1
                points += 1
            elif counter != 0 and board[row][col] != 0:
                board[row - counter][col] = board[row][col]
                board[row][col] = 0
    return [board, points]


def repopulate(board):
    for i in range(9):
        for j in range(7):
            if board[i][j] == 0:
                board[i][j] = random.randint(1, 7)
    return board


def show_points(points):
    stddraw.setFontSize(40)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.text(1, -0.5, "Score: "+str(points))


def show_turns(turn):
    stddraw.setFontSize(40)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.text(4, -0.5, "Turn: "+str(turn))


def show_end():
    stddraw.setFontSize(125)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.text(3.5, 4.5, "Game Over")
    stddraw.show()