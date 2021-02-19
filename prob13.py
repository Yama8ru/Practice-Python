def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Enter number: '))
res = [fibonacci(i) for i in range(n)]
for i in res: 
    print(i)
