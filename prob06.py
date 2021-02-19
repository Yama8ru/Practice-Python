string = input('Enter a string: ')
if string == string[::-1]:
    print(f'{string} is palindrome')
else:
    print(f'{string} isn\'t palindrome')

