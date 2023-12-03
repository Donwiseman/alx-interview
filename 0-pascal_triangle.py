""" Has two function, A factorial function and a pascal triangle function."""


def factorial(n):
    """ Returns the nth factorial. """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def pascal_triangle(n):
    """ Returns a list containing n rows of a pascal triangle. """
    if n < 0:
        return []
    pascal_list = []
    for row in range(n):
        if row == 0:
            pascal_list.append([1])
            continue
        row_list = []
        for column in range(row + 1):
            element = factorial(row)/(factorial(column) *
                                      factorial(row - column))
            row_list.append(int(element))
        pascal_list.append(row_list)
    return pascal_list
