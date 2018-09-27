'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
[3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''


def product_of_others(in_list):
    rtrn = []
    total = in_list[0]
    for x in range(1,len(in_list)):
        total *= in_list[x]
    for y in range(0,len(in_list)):
        rtrn.append(int(total/in_list[y]))
    return rtrn


def product_of_others_followup(in_list):
    rtrn = []
    for x in in_list:
        append = 1
        for y in in_list:
            if y != x:
                append *= y
        rtrn.append(append)
    return rtrn


print(product_of_others([1, 2, 3, 4, 5]))
print(product_of_others([3,2,1]))
print(product_of_others_followup([1, 2, 3, 4, 5]))
print(product_of_others_followup([3, 2, 1]))
