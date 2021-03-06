import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_min_city_chicken_distance(n, m, city_map):
    chicken_locations = []
    home_locations = []

    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                home_locations.append((i, j))
            elif city_map[i][j] == 2:
                chicken_locations.append((i, j))

    chicken_location_m_combinations = list(itertools.combinations(chicken_locations, m))
    print(chicken_location_m_combinations)
    min_distance_of_m_combinations = sys.maxsize
    for chicken_location_m_combination in chicken_location_m_combinations:
        distance = 0
        for home_r, home_c in home_locations:
            min_distance = sys.maxsize
            for chicken_r, chicken_c in chicken_location_m_combination:
                min_distance = min(min_distance, abs(home_r - chicken_r) + abs(home_c - chicken_c))
            distance += min_distance
        print("distance", distance)
        min_distance_of_m_combinations = min(min_distance_of_m_combinations, distance)

    return min_distance_of_m_combinations


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!