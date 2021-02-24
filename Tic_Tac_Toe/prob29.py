from prob26 import check

def draw_board(board_list):
    for i in range(3):
        print(' ---' * 3)
        for j in board_list[i]:
            if j == 0:
                print('|   ', end='')
            else:
                print(f'| {j} ', end='')
        print('|')
    print(' ---' * 3)

def enter_position():
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    used_position = []
    while True:
        X_row, X_col = tuple(map(lambda i: int(i)-1, \
                input('Player1, Enter position (row, col): ').split(',')))
        if (X_row, X_col) not in used_position:
            used_position.append((X_row, X_col))
            game[X_row][X_col] = 'X'
        draw_board(game)

        if winner := check(game):
            return winner

        O_row, O_col = tuple(map(lambda i: int(i)-1, \
                input('Player2, Enter position (row, col): ').split(',')))
        if (O_row, O_col) not in used_position:
            used_position.append((O_row, O_col))
            game[O_row][O_col] = 'O'
        draw_board(game)

        if winner := check(game):
            return winner

if __name__ == '__main__':
    res = enter_position()
    if res == 'X':
        print('Winner is player1')
    elif res == 'O':
        print('Winner is player2')
