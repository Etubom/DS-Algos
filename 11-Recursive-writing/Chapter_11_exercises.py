
# Use recursion to write a function that accepts an array of strings and returns the total number
# of characters across all the strings.For example,if the input is ["ab","c","def","ghij"] the output should
# be 10 since there are 10 characters in total.

def total_array_characters(array):
    if len(array) == 0:
        return 0
    else:
        return len(array[0]) + total_array_characters(array[1:])

# print(total_array_characters(["ab","c","def","ghij"]))


# Use recursion to write a function that accepts an array of numbers and
# returns a new array containing just the even numbers

def get_even_numbers(array):
    if len(array) == 0:
        return []
    elif array[0] % 2 == 0:
        return [array[0]] + get_even_numbers(array[1:])
    else:
        return get_even_numbers(array[1:])

arr = [1,2,3,4,5,6]
# print(get_even_numbers(arr))

# There is a numerical sequence known as "Triangular Numbers" The pattern begins
# as 1,3,6,10,15,21 and continues onwards with the Nth number in the pattern,
# which is N plus the previous number.For example,the 7th number in the sequence
# is 28, since it's 7 (which is N) plus 21 (the previous number in the sequence).
# Write a function that accepts a number for N and returns the correct number from the series.
# Thats is, if the function was passed the number 7,the function would return 28.
def triangular_numbers(n):
    if n == 1:
        return 1
    else:
        return n + triangular_numbers(n - 1)

# print(triangular_numbers(7))

# Use recursion to write a function that accepts a string and returns the
# first index that contains the character "x".For example,the string
# "abcdefghijklmnopqrstuvwxyz" has an "x" at index 23.To keep things
# simple,assume the string definitely has at least one "x".

def index_of_x(str):
    # i = 0
    if str[0] == 'x':
        return 0
    else:
        return index_of_x(str[1:]) + 1
#
letters = "abcdefghijklmnopqrstuvwxyz"

print(index_of_x(letters,))


