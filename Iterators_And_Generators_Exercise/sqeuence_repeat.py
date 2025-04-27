class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current_length = -1


    def __iter__(self):
        return self

    def __next__(self):
        if self.current_length == self.number - 1:
            raise StopIteration

        self.current_length += 1

        return self.sequence[self.number % len(self.sequence)]


iterator = sequence_repeat('asd', 3)
for el in iterator:
    print(el)
