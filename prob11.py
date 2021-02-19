def check_primer(n):
    res = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            res = False
            break
    return res

number = int(input('Enter number: '))
print('prime' if check_primer(number) else 'not prime')
