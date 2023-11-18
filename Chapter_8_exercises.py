

def check_for_intersection_values(array1, array2):
    hashtable = {}
    result = []
    for value in array1:
        hashtable[value] = True

    for item in array2:
        if item in hashtable:
            result.append(item)

    return result


# print(check_for_intersection_values([1, 2, 3, 4, 5], [0, 2, 4, 6, 8]))


def find_first_duplicate(string_array):
    hashtable = {}
    for value in string_array:
        if value in hashtable:
            return value
        else:
         hashtable[value] = True


# print(find_first_duplicate(["a","b","c","d","c","e"]))

# def check_if_alphabet_letter_missing(str):
#     alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     str_array = list(str)
#     hashtable = {}
#     missing_letter = None
#
#     for value in alphabets:
#         hashtable[value] = True
#
#     for value in str_array:
#         if value not in hashtable:
#             missing_letter = value
#             break
#
#     return missing_letter
#
# print(check_if_alphabet_letter_missing("the quick brown box jumps over a lazy dog"))
def check_if_alphabet_letter_missing(str):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    str_array = list(str.lower())  # Convert input string to lowercase for case-insensitive comparison
    hashtable = {}

    for value in alphabets:
        hashtable[value] = False  # Initialize all letters as False


    for value in str_array:
        if value in hashtable:
            hashtable[value] = True  # Mark the letter as present

    # missing_letters = [letter for letter, present in hashtable.items() if not present]
    missing_letters = [letter for letter in hashtable if not hashtable[letter]]
    if missing_letters:
        return missing_letters[0]  # Return the first missing letter
    else:
        return None  # If all letters are present, return None


# print(check_if_alphabet_letter_missing("the quick brown box jumps over a lazy dog"))


def find_first_non_duplicated_character(str):
    count = 1
    hashtable = {}
    list_of_non_dups = []
    target = 1
    str_array = list(str.lower())

    for value in str_array:
        if value not in hashtable:
            hashtable[value] = count
        else:
            hashtable[value] += 1  # Increment the count for duplicated characters

    for key, value in hashtable.items():
        if value == target:
            list_of_non_dups.append(key)

    if list_of_non_dups:  # Check if there are any non-duplicated characters
        return list_of_non_dups[0]  # Return the first non-duplicated character
    else:
        return None  # Return None if there are no non-duplicated characters


print(find_first_non_duplicated_character("minimum"))



