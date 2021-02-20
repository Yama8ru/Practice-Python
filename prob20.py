import random
def element_search(num_list, num):
    print(f'{num} exist in {num_list}' if num in num_list else f'{num} don\'t exist in {num_list}')

num_list = [random.randint(0, 10) for i in range(10)]
num = random.randint(0, 10)
element_search(num_list, num)
