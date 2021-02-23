def draw_board(size):
    for i in range(size):
        print(' ---' * size)
        print('|   ' * size, end='')
        print('|')
    print(' ---' * size)

if __name__ == '__main__':
    size = int(input('Enter board size: '))
    draw_board(size)
