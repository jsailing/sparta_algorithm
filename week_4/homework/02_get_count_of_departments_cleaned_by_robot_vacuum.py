current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# d: 0 - N, 1 - E, 2 - S, 3 - W
# delta value for N E S W
#      N  E  S  W
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def get_new_r_c_d_when_turning_left(r, c, d):
    # N -> W: 0 -> 3
    # E -> N: 1 -> 0
    # S -> E: 2 -> 1
    # W -> S: 3 -> 2

    d = (d + 3) % 4
    r, c = r + dr[d], c + dc[d]
    return r, c, d


def get_new_r_c_when_reversing(r, c, d):
    # N -> S: 0 -> 2
    # E -> W: 1 -> 3
    # S -> N: 2 -> 0
    # W -> E: 3 -> 1

    d = (d + 2) % 4
    r, c = r + dr[d], c + dc[d]
    return r, c


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    cleaned_with_numbering = 2
    count_of_departments_cleaned = 1
    room_map[r][c] = cleaned_with_numbering
    queue = list([(r, c, d)])

    while True:
        r, c, d = queue[0]
        new_d = d

        for i in range(4):  # 4 directions: N E S W
            new_r, new_c, new_d = get_new_r_c_d_when_turning_left(r, c, new_d)  # with new d

            if room_map[new_r][new_c] == 0:
                count_of_departments_cleaned += 1
                cleaned_with_numbering += 1
                room_map[new_r][new_c] = cleaned_with_numbering
                queue[0] = (new_r, new_c, new_d)
                break
            elif i == 3:
                new_r, new_c = get_new_r_c_when_reversing(r, c, d)  # with current d

                if room_map[new_r][new_c] == 1:  # if wall
                    return count_of_departments_cleaned

                queue[0] = (new_r, new_c, d)

    return


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))

for i in range(len(current_room_map)):
    print(current_room_map[i])