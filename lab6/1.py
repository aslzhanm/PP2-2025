from functools import reduce

def multiply_list(lst):
    return reduce(lambda x, y: x * y, lst)

print(multiply_list([1, 2, 3, 4, 5]))
