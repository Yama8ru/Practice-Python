import random

while True:
    number = random.randint(1, 9)
    ans = input('Your answar: ')
    if ans == 'exit':
        break
    elif number == int(ans):
        print('correct')
    elif number > int(ans):
        print('smaller')
    elif number < int(ans):
        print('bigger')
