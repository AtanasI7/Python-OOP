class vowels:
    def __init__(self, string: str):
        self.string = string
        self.vowels = ['a', 'e', 'i', 'y', 'u', 'o']
        self.index = -1
        self.vowels_values = [m for m in self.string if m.lower() in self.vowels]
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1

        if self.index < len(self.vowels_values):
            return self.vowels_values[self.index]

        raise StopIteration
        
