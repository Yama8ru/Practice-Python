with open('primenumbers.txt', 'r', encoding='UTF-8') as f:
    prime_nums = {i.rstrip('\n') for i in f.readlines()}

with open('happynumbers.txt', 'r', encoding='UTF-8') as f:
    happy_nums = {i.rstrip('\n') for i in f.readlines()}

print(prime_nums & happy_nums)
