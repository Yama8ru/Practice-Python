name_count = {}
with open('namelist.txt', 'r', encoding='UTF-8') as f:
    for row in f.readlines():
        name = row.rstrip('\n')
        if name not in name_count:
            name_count[name] = 1
        name_count[name] += 1

for key, value in name_count.items():
    print(f'{key}: {value}')
