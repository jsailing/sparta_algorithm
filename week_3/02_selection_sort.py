input = [4, 6, 2, 9, 1]

"""
[4, 6, 2, 9, 1]
 s  -  s  -  -  ; selected index = 0 -> 2
[1, 6, 2, 9, 4] ; 0 <-> 2
    s  s  -  -  ; selected index = 1 -> 2
[1, 2, 6, 9, 4] ; 1 <-> 2
       s  -  s  ; selected index = 2 -> 4
[1, 2, 4, 9, 6] ; 2 <-> 4
          s  s  ; selected index = 3 -> 4
[1, 2, 4, 6, 9] ; 3 <-> 4
"""


def selection_sort(array):
    n = len(array)
    for i in range(n - 1):  # O(N)
        min_index = i
        for j in range(1, n - i):  # O(N)
            print(i+j)
            if array[i + j] < array[min_index]:
                min_index = i + j

        array[i], array[min_index] = array[min_index], array[i]

    return


"""
def selection_sort(array):
    n = len(array)
    for i in range(n): # O(N)
        min_index = i
        for j in range(n - i): # O(N)
            if array[i + j] < array[min_index]:
                min_index = i + j

        array[i], array[min_index] = array[min_index], array[i]

    return
"""

selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!