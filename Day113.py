"""
Problem:

Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return
"here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?
"""

"""
Process:

1. Split string into a list using space as the delimiter
2. Create string to store output into
3. Iterate over word list backwards appending the contents of the array to the string as well as a space if it isn't
    the last word
4. Return output

Process 2:

1. Split string into array using space as delimiter
2. Reverse the contents of the array
3. Set output to " ".join(word_list) on the array to get a string of the contents of the array separated by spaces
4. Return output

Process 3:

1. Do everything in process 2, except do it in one line by using the reversed operator to reverse the list

Followup:

1. Reverse entire string
2. Find beginning and end of each word
3. Iterate over each character in each word, swapping the characters at the beginning and end of the word and working
    towards the middle
"""


def reverse_words(string_of_words):
    output = ""
    word_list = string_of_words.split(' ')
    for x in range(len(word_list) - 1, -1, -1):
        output += word_list[x]
        if x != 0:
            output += ' '
    return output


def reverse_words_two(string_of_words):
    word_list = string_of_words.split(' ')
    word_list.reverse()
    output = " ".join(word_list)
    return output


def reverse_words_three(string_of_words):
    return " ".join(reversed(string_of_words.split(' ')))


def reverse_words_followup(string_of_words):
    string_of_words.reverse()
    start = 0
    for counter, value in enumerate(string_of_words):
        # Find te indices of the first and last character of a word
        if value == ord(' '):
            new_start = counter + 1
            end = counter - 1
        elif counter == len(string_of_words) - 1:
            end = counter
        else:
            continue

        while start < end:
            string_of_words[start], string_of_words[end] = string_of_words[end], string_of_words[start]
            start += 1
            end -= 1

        # Prepare for the next word
        start = new_start

    return string_of_words


print(reverse_words("hello world here"))
print(reverse_words_two("hello world here"))
print(reverse_words_three("hello world here"))
print(reverse_words_followup(bytearray(b"hello world here")).decode('ASCII'))
