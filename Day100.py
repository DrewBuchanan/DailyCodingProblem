"""
Problem:

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)

You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps
in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2

It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
"""

"""
Process:

1. Creating an array to represent the grid is a trap.
2. Since there are no obstacles and all points are traversable, we don't need to worry about implementing actual 
pathfinding.
3. In order to get the steps between points A and B, you must find the number of steps to take diagonally, then add the 
number of steps in one direction to get to the point.
4. Number of diagonal steps can be found by:
    diagonalSteps = min(abs(Ax - Bx), abs(Ay - By))
    We take the minimum here because it the smaller of the differences is the maximum number of diagonal steps we can
    take, otherwise, we potentially miss the point.
5. Number of cardinal steps can be found by:
    cardinalSteps = abs(max(abs(Ax - Bx), abs(Ay - By)) - diagonalSteps)
    Here, we want the difference we didn't use, then by subtracting the number of steps we took diagonally, we will get
    the number of steps we need to take in a cardinal direction
6. steps += diagonalSteps + cardinalSteps
7. Repeat for each pair of points
"""


def steps_between_points(points):
    start = points[0]
    steps = 0
    a = start
    for x in range(1, len(points)):
        b = points[x]
        diagonal_steps = min(abs(a[0] - b[0]), abs(a[1] - b[1]))
        cardinal_steps = abs(max(abs(a[0] - b[0]), abs(a[1] - b[1])) - diagonal_steps)
        steps += diagonal_steps + cardinal_steps
        a = b
    return steps


print(steps_between_points([(0, 0), (1, 1), (2, 2)]))
# Test negative numbers
assert(steps_between_points([(0, 0), (-1, -1), (-2, -2)]) == 2)
# Test using both cardinal and diagonal steps
assert(steps_between_points([(0, 0), (3, 4), (5, 6)]) == 6)
