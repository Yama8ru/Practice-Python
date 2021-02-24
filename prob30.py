import random

with open('./sowpods.txt', 'r', encoding='utf-8') as f:
    words = [word for word in f.read().rsplit('\n')]

index = random.randint(0, len(words)-1)
print(words[index])
