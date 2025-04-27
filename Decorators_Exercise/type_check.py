def type_check(obj_type):
    def decorator(function):
        def wrapper(*args, **kwargs):
            given_input = args[0]

            if not isinstance(given_input, obj_type):
                return "Bad Type"

            return function(*args, **kwargs)

        return wrapper

    return decorator



@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

