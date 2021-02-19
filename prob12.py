a = [5, 10, 15, 20, 25]
def new_list(arg):
    res = []
    res.append(a[0])
    res.append(a[-1])
    return res
b = new_list(a)
print(b)
