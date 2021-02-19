import random

def dupe_set(arg):
    res = list(set(arg))
    return res

def dupe_loop(arg):
    res = []
    for i in arg:
        if i in res:
            continue
        else:
            res.append(i)
    return res

a = [random.randint(0, 10) for i in range(10)]
print(a)
print(dupe_set(a))
print(dupe_loop(a))
