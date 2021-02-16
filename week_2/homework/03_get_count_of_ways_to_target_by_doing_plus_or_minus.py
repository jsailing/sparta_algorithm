numbers = [1, 1, 1, 1, 1]
target_number = 3
count_of_ways = 0


def get_count_of_ways_to_target(array, array_size, target, current_index, current_sum):
    if current_index == array_size:
        if current_sum == target:
            global count_of_ways
            count_of_ways += 1
        return

    get_count_of_ways_to_target(
        array, array_size, target, current_index + 1, current_sum - numbers[current_index]
    )
    get_count_of_ways_to_target(
        array, array_size, target, current_index + 1, current_sum + numbers[current_index]
    )


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    get_count_of_ways_to_target(array, len(array), target, 0, 0)
    return count_of_ways


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!