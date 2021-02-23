def enter_position():
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    used_position = []
    while True:
        if len(used_position) == 9:
            break

        X_row, X_col = tuple(map(lambda i: int(i)-1, \
                input('Player1, Enter position (row, col): ').split(',')))
        if (X_row, X_col) not in used_position:
            used_position.append((X_row, X_col))
            game[X_row][X_col] = 'X'
        print(game)

        O_row, O_col = tuple(map(lambda i: int(i)-1, \
                input('Player2, Enter position (row, col): ').split(',')))
        if (O_row, O_col) not in used_position:
            used_position.append((O_row, O_col))
            game[O_row][O_col] = 'O'
        print(game)

if __name__ == '__main__':
    enter_position()


