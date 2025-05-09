n = int(input())

def print_row(size, row):
    print(" " * (size - row), "* " * row)

def print_upper_rhombus_part(size):
    for row in range(1, n + 1):
        print_row(size, row)

def print_lower_rhombus_part(size):
    for row in range(n - 1, 0, -1):
        print_row(size, row)

def print_rhombus(size):
    print_upper_rhombus_part(size)
    print_lower_rhombus_part(size)

print_rhombus(n)



