def judge(board_list):
    win_player1, win_player2 = False, False
    for i in range(3):
        if board_list[0][i] == board_list[1][i] \
                and board_list[1][i] == board_list[2][i]:
                    if board_list[0][i] == 1:
                        win_player1 = True
                    else:
                        win_player2 = True
                    break

    for i in range(3):
        if board_list[i][0] == board_list[i][1] \
                and board_list[i][1] == board_list[i][2]:
                    if board_list[0][i] == 1:
                        win_player1 = True
                    else:
                        win_player2 = True
                    break

    if board_list[0][0] == board_list[1][1] \
            and board_list[1][1] == board_list[2][2]:
                    if board_list[0][0] == 1:
                        win_player1 = True
                    else:
                        win_player2 = True

    if board_list[0][2] == board_list[1][1] \
            and board_list[1][1] == board_list[2][0]:
                    if board_list[0][2] == 1:
                        win_player1 = True
                    else:
                        win_player2 = True

    return win_player1, win_player2

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

    one, two = judge(winner_is_1)
    print('Winner is 1' if one else 'Winner is 2')
