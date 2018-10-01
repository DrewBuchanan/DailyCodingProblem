import random

"""
Problem:

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function
rand5() that returns an integer from 1 to 5 (inclusive).
"""

"""
Process:

Step 1: Implement rand7 for testing purposes

Step 2: Define rand5 by calling rand7 until it returns a number between 1 and 5. This could theoretically go on forever,
so that's probably not feasible for use

Step 3: Define rand5 by taking the remainder of rand7 divided by 5 and adding 1 to prevent generating 0. This is not a
uniform distribution however as 2 numbers are effectively generated twice as often.

There's definitely a way to make the distribution from Step 3 uniform, but I can't figure it out at the moment. I'll
come back to this one.
"""


def rand7():
    return random.randint(1, 7)


'''
Step 2
def rand5():
    rand = rand7()
    while rand > 5:
        rand = rand7()
    return rand
'''

'''
Step 3
'''


def rand5():
    return rand7() % 5 + 1


results = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0
}
for i in range(1, 100000):
    rand = rand5()
    results[rand] += 1

print(results)
