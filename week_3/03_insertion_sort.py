input = [4, 6, 2, 9, 1]

"""
[4, 6, 2, 9, 1]
  <>            # indexing: 1 -> 0
[4, 6, 2, 9, 1]
  <> <>         # indexing: 2 -> 0
[2, 4, 6, 9, 1]
        <>      # indexing: 3 -> 0
[2, 4, 6, 9, 1] # no swapping
  <> <> <> <>   # indexing: 4 -> 0
[1, 2, 4, 6, 9]
"""


# max O(N^2)
# min 0(N) by "break"
def insertion_sort(array):
    n = len(array)
    for i in range(n - 1):  # O(N)
        for j in range(i + 1):  # O(N)
            if array[i - j] > array[i - j + 1]:
                array[i -j], array[i - j + 1] = array[i - j + 1], array[i - j]
            else:
                break

    return


insertion_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
