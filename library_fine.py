# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 03:36:28 2015
Library Fine Problem Statement:

The Head Librarian at a library wants you to make a program that
calculates the fine for returning the book after the return date.
You are given the actual and the expected return dates.
Calculate the fine as follows:

If the book is returned on or before the expected return date,
no fine will be charged, in other words fine is 0.
If the book is returned in the same month as the expected return date,
Fine = 15 Hackos × Number of late days
If the book is not returned in the same month but in the same year as
the expected return date, Fine = 500 Hackos × Number of late months
If the book is not returned in the same year, the fine is fixed at 10000 Hackos
Input Format

You are given the actual and the expected return dates in D M Y format
respectively.
There are two lines of input. The first line contains the D M Y values for the
actual return date and the next line contains the D M Y values for the expected
return date.

Constraints
1≤D≤31
1≤M≤12
1≤Y≤3000
Output Format
Output a single value equal to the fine.
Sample Input

9 6 2015
6 6 2015
Sample Output
45

Explanation

Since the actual date is 3 days later than expected, fine is calculated as
15×3=45 Hackos.
@author: Rafeh
"""
from collections import namedtuple


def fee(book_return_date, book_due_date):

    '''
    Take book return date and book due date as input, return the fine.
    >>> fee('9 9 2015', '6 9 2015')
    45
    >>> fee('9 9 2015', '6 9 2013')
    10000
    >>> fee('9 9 2015', '6 8 2015')
    500
    >>> fee('9 9 2015', '9 9 2015')
    0
    >>> fee('9 9 2015', '6 7 2015')
    1000
    >>> fee('9 9 2015', '6 11 2014')
    10000
    >>> fee('28 2 2015', '15 4 2015')
    0
    '''
    Date = namedtuple('Date', ['day', 'month', 'year'])
    due = Date(*map(int, book_due_date.split()))
    book_return = Date(*map(int, book_return_date.split()))

    if book_return.year > due.year:
        fine = 10000

    elif book_return.year < due.year:
        fine = 0

    elif book_return.month > due.month:
        fine = 500 * (book_return.month - due.month)

    elif book_return.month < due.month:
        fine = 0

    elif book_return.day > due.day:
        fine = 15 * (book_return.day - due.day)

    elif book_return.day < due.day:
        fine = 0

    else:
        fine = 0

    return fine


if __name__ == '__main__':
    import doctest
    doctest.testmod()
