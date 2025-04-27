def make_bold(function):
    def wrapper(*args, **kwargs):
        return f"<b>{function(*args, **kwargs)}</b>"

    return wrapper


def make_italic(function):
    def wrapper(*args, **kwargs):
        return f"<i>{function(*args, **kwargs)}</i>"

    return wrapper


def make_underline(function):
    def wrapper(*args, **kwargs):
        return f"<u>{function(*args, **kwargs)}</u>"

    return wrapper

@make_italic
@make_underline
@make_bold
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
