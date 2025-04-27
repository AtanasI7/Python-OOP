# class store_results:
#
#     def __call__(self, *args, **kwargs):
#          with open("files/log.txt", "a") as log_file:
#             log_file.write(
#                 f"Function {func.__name__} was called and the result is {func(*args, **kwargs)}\n"
#             )

def store_results(func):
    def wrapper(*args, **kwargs):
        with open("files/log.txt", "a") as log_file:
            log_file.write(
                f"Function {func.__name__} was called and the result is {func(*args, **kwargs)}\n"
            )

    return wrapper



@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
