def vowel_filter(function):
    VOWELS = ['a', 'e', 'y', 'o', 'u', 'i']

    def wrapper():
        result = function()
        return [el for el in result if el in VOWELS]

    return wrapper

@vowel_filter
def get_letters():
    return ['a', 'b', 'c', 'd', 'e']

print(get_letters())