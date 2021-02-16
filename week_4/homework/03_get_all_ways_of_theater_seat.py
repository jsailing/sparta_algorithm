seat_count = 9
vip_seat_array = [4, 7]

memo = {
    1: 1,
    2: 2
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    partial_ways = 0
    all_way = 1
    current_seat = 1

    for fixed_seat in fixed_seat_array:
        partial_ways = fibo_dynamic_programming(fixed_seat - current_seat, memo)
        all_way *= partial_ways
        current_seat = fixed_seat + 1

    partial_ways = fibo_dynamic_programming(total_count + 1 - current_seat, memo)
    all_way *= partial_ways

    return all_way


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))