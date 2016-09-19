# number of test cases.
T = int(input())


def find_digits(number):
    """
    takes in a string of number and returns the total count of digits
    that the number is divisible by.
    Note: The divisibility is only checked of the digits
    that are inside number.
    :param: string
    :return: number
    >>> find_digits('122')
    3
    >>> find_digits('1012')
    3
    """
    counter = 0
    for digit in number:
        if int(digit) and int(number) % int(digit) == 0:
            counter += 1
    return counter

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    for _ in range(T):
        print(find_digits(input()))
