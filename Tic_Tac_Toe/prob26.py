def check(grid):
    # row
    for i in range(3):
        row = set([grid[i][0], grid[i][1], grid[i][2]])
        if len(row) == 1 and grid[i][0] != 0:
            return grid[i][0]

    # column
    for i in range(3):
        column = set([grid[0][i], grid[1][i], grid[2][i]])
        if len(column) == 1 and grid[0][i] != 0:
            return grid[0][i]

    # diagonal
    if grid[1][1] != 0:
         diagonal_1 = set([grid[0][0], grid[1][1], grid[2][2]])
         diagonal_2 = set([grid[0][2], grid[1][1], grid[2][0]])
         if len(diagonal_1) == 1 or len(diagonal_2) == 1:
             return grid[1][1]

if __name__ == '__main__':
    winner_is_2 = [[2, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]

    winner_is_1 = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]

    winner_is_also_1 = [[0, 1, 0],
            [2, 1, 0],
            [2, 1, 1]]

    no_winner = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 2]]

    also_no_winner = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 0]]

    print(f'winner is {check(winner_is_2)}')
    print(f'winner is {check(winner_is_1)}')
    print(f'winner is {check(winner_is_also_1)}')
    print(f'winner is {check(no_winner)}')
    print(f'winner is {check(also_no_winner)}')
