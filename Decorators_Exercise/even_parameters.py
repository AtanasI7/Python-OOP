def even_parameters(function):
    def wrapper(*args, **kwargs):
        for el in args:
            if not isinstance(el, int):
                return "Please use only even numbers!"

            if el % 2 != 0:
                return "Please use only even numbers!"

            continue

        result = function(*args, **kwargs)

        return result

    return wrapper




@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))

# @even_parameters
# def multiply(*nums):
#     result = 1
#     for num in nums:
#         result *= num
#     return result
#
# print(multiply(2, 4, 6, 8))
# print(multiply(2, 4, 9, 8))

