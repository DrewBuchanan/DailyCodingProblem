'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''


def sum_of_any_two_equals_k(in_list, k):
    for x in in_list:
        if k - x in in_list:
            return True
    return False


print(sum_of_any_two_equals_k([10, 15, 3, 7], 17))
print(sum_of_any_two_equals_k([3,4,5], 100))
