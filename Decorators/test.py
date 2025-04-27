increase_number = int(input())


def increase(num):

    def decorator(function):

        def wrapper():
            result = function()

            return [el + num for el in result]

        return wrapper

    return decorator


@increase(increase_number)
def get_numbers():
    return [2, 7, 3]

print(get_numbers())