input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        alphabet_occurrence_array[ord(char) - ord('a')] += 1

    max_occurrence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet_occurrence_array)):
        occurrence = alphabet_occurrence_array[index]

        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alphabet_index = index

    return chr(ord('a') + max_alphabet_index)


result = find_max_occurred_alphabet(input)
print(result)
