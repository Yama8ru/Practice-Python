import random

class Password:
    SYMBOLS = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        ['!', '"', '\'', '#', '$', '%', '&', '‘', '(', ')', '*', '+', ',', '-', '.', '//', ':', ':', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]

    def __init__(self, password_size):
        self.password_size = password_size

    def gen_password(self):
        password = ''
        for i in range(self.password_size):
            row = random.randint(0,2)
            column = random.randint(0,len(self.SYMBOLS[row])-1)
            password += password.join(self.SYMBOLS[row][column])
        return password

if __name__ == '__main__':
    user_size = int(input('Enter Password size: '))
    obj = Password(user_size)
    print(f'Generated Password: {obj.gen_password()}')

