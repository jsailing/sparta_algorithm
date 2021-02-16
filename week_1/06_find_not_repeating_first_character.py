input = "abadabac"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        alphabet_occurrence_array[ord(char) - ord('a')] += 1

    for char in string:
        char_index = ord(char) - ord('a')
        if alphabet_occurrence_array[char_index] == 1:
            return char

    # not_repeating_character_array = []
    # for index in range(len(alphabet_occurrence_array)):
    #     if alphabet_occurrence_array[index] == 1:
    #         not_repeating_character_array.append(chr(ord('a') + index))
    #
    # print(not_repeating_character_array)
    #
    # for char in string:
    #     if char in not_repeating_character_array:
    #         return char

    return '_'


result = find_not_repeating_character(input)
print(result)
