def logged(function):
    def wrapper(*args, **kwargs):
        name_of_func = function.__name__
        nums = function(*args)

        result = [f"you called {name_of_func}{args}", f"it returned {str(nums)}"]

        return '\n'.join(result)
    return wrapper



@logged
def func(*args):
    return 3 + len(args)

print(func(4, 4, 4))

