import random

def max_of_three(a, b, c):
    max_val = -1
    if a >= b:
        if a >= c:
            max_val = a
        else:
            max_val = c
    elif b >= a:
        if b >= c:
            max_val =  b
        else:
            max_val = c
    return max_val

if __name__ == '__main__':
    a, b, c = (random.randint(0,9) for i in range(3))
    print(a, b, c)
    print(max_of_three(a, b, c))
