def strict(func):
    def wrapper(*args):
        func_type = func.__annotations__
        if func_type['a'] == type(args[0]) and func_type['b'] == type(args[1]):
            return func(*args)
        else:
            #raise TypeError
            return 'TypeError'
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
print(sum_two(1.0, 2))  # >>> TypeError
print(sum_two(1, False))  # >>> TypeError
print(sum_two(True, 5.4))  # >>> TypeError
print(sum_two(10, 17))  # >>> 27
print(sum_two(1, '3'))  # >>> TypeError
