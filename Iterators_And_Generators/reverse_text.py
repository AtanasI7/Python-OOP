def reverse_text(some_text):
    start = 1
    while start <= len(some_text):
        yield some_text[-start]
        start += 1

