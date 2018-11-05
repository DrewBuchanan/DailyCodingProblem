"""
Problem:

Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped,
the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?
"""

"""
Process:

1. Convert given binaries to integers
    10101010 = 170
    11100010 = 226
    
2. Use bin to get a string from the integer
3. Create a substring that removes the first 2 characters to be left with the bits
4. Replace all 0s with 2s
5. Replace all 1s with 0s
6. Replace all 2s with 1s
"""

print(bin(170)[2:].replace('0','2').replace('1','0').replace('2','1'))
