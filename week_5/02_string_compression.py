input = "abcabcabcabcdededededede"


def string_compression(string):
    compressed_string_lengths_array = []

    n = len(string)
    for split_size in range(1, n // 2):
        # splited_string_array = []
        # for i in range(0, n, split_size):
        #     splited_string_array.append(string[i: i + split_size])

        compressed_string = ""
        splited_string_array = [string[i: i + split_size] for i in range(0, n, split_size)]

        count = 1
        for j in range(0, len(splited_string_array) - 1):
            cur, next = splited_string_array[j], splited_string_array[j + 1]

            if cur == next:
                count += 1
            else:
                if count > 1:
                    compressed_string += str(count)
                compressed_string += cur
                count = 1

        if count > 1:
            compressed_string += str(count)
        compressed_string += splited_string_array[-1]

        print(compressed_string)

        compressed_string_lengths_array.append(len(compressed_string))

    return min(compressed_string_lengths_array)


print(string_compression(input))  # 14 가 출력되어야 합니다!
