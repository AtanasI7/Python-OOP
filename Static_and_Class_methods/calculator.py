from functools import reduce


class Calculator:

    @staticmethod
    def add(*nums):
        return sum(nums)

    @staticmethod
    def multiply(*nums):
        return reduce(lambda a, b: a * b, nums)

    @staticmethod
    def subtract(*nums):
        return reduce(lambda a, b: a - b, nums)

    @staticmethod
    def divide(*nums):
        return reduce(lambda a, b: a / b, nums)