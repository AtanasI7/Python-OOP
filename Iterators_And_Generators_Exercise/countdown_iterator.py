class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.temp = self.count + 1

    def  __iter__(self):
        self.temp = self.count + 1
        return self

    def __next__(self):
        if self.temp == 0:
            raise StopIteration

        self.temp -= 1

        return self.temp

iterator = countdown_iterator(10)
for item in iterator:
    print(item)

for item in iterator:
    print(item)