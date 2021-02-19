def reverse_str():
    words = input('Enter words: ').split(' ')
    for word in words[::-1]:
        print(word, end=' ')
    print()

reverse_str()
