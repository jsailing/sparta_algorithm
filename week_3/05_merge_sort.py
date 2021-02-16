array = [5, 3, 2, 1, 6, 8, 7, 4]

# N
# 1: N/2 * 2
# 2: N/2^2 * 4
# 3: N/2^3 * 8
# .: ...
# k: 1
# k = log2N
# O(logN * N) = O(NlogN)


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    print(array)
    return merge(left_array, right_array)  # O(N)


def merge(array1, array2):  # O(N)
    # len(array) = len(array1) + len(array2)
    # O(N) = O(N1) + O(N2)
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!