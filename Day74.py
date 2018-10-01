"""
Problem:

Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and j-th
column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X appears as a value in an N by N
multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

| 1 | 2 | 3 | 4 | 5 | 6 |

| 2 | 4 | 6 | 8 | 10 | 12 |

| 3 | 6 | 9 | 12 | 15 | 18 |

| 4 | 8 | 12 | 16 | 20 | 24 |

| 5 | 10 | 15 | 20 | 25 | 30 |

| 6 | 12 | 18 | 24 | 30 | 36 |

And there are 4 12's in the table.
"""

"""
Process:

Step 1: Brute-Force

Iterate over the entire table and increment a variable when we find an instance of x
O(N^2)

Step 2: Use modulo operator

Iterate over one axis, then count the number of times the remainder of x/y is 0

O(N)

Step 3: Use modulo over half of axis

If we iterate over half of the axis, we can increment the counter by 2 because if we find a multiple early in the axis,
it's inverse will also be on the table

O(N/2)

"""


def step_one(n, x):
    counter = 0
    for y in range(2, n + 1):
        for z in range(2, n + 1):
            if y * z == x:
                counter += 1
    return counter


def step_two(n, x):
    counter = 0
    for y in range(2, n + 1):
        if x % y == 0:
            counter += 1
    return counter


def step_three(n, x):
    counter = 0
    for y in range(2, int(n/2)+1):
        if x % y == 0:
            counter += 2
    return counter


print(step_one(6, 12))
print(step_two(6, 12))
print(step_three(6,12))
