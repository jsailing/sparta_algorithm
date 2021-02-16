k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

# 말은 순서대로 이동 -> 말의 순서에 따라 반복문
# 말이 쌓일 수 있다 -> 맵에 말이 쌓이는 걸 저장
# 쌓이 순서대로 이동 -> 스택

# 현재 맵에 말이 쌓여 있는 정보기 필요.


def get_new_d_index_when_go_back(d):
    # 0 -> 1 : 0
    # 1 -> 0 : 1
    # 2 -> 3 : 0
    # 3 -> 2 : 1
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(game_map)
    turn_count = 1
    current_stacked_horse_map = [[[] for _ in range(n)] for _ in range(n)]

    # 말의 위치를 초기화
    for index in range(horse_count):
        r, c, d = horse_location_and_directions[index]
        current_stacked_horse_map[r][c].append(index)

    print("init")
    for i in range(len(current_stacked_horse_map)):
        print(current_stacked_horse_map[i])

    while turn_count <= 1000:
        for horse_index in range(horse_count):
            n = len(game_map)
            r, c, d = horse_location_and_directions[horse_index]
            new_r = r + dr[d]
            new_c = c + dc[d]

            # 파란색이거나 범위를 벗어나는 경
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_new_d_index_when_go_back(d)

                horse_location_and_directions[horse_index][2] = new_d
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]
                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue

            # 이동할 말들을 구하고 current_stacked_horse_map 갱신
            moving_horse_index_array = []
            for i in range(len(current_stacked_horse_map[r][c])):
                index = current_stacked_horse_map[r][c][i]
                if index == horse_index:
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:]
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]
                    break

            # 빨간섹 - 이동할 말들의 순서를 반대로 바꿈
            if game_map[new_r][new_c] == 1:
                moving_horse_index_array = reversed(moving_horse_index_array)

            # 새 위치와 함께 horse map 갱신 및 이동하는 말들의 위치 갱신
            for index in moving_horse_index_array:
                current_stacked_horse_map[new_r][new_c].append(index)
                horse_location_and_directions[index][0], horse_location_and_directions[index][1] = new_r, new_c

            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                print("succeed")
                for i in range(len(current_stacked_horse_map)):
                    print(current_stacked_horse_map[i])
                return turn_count

        print("turning")
        for i in range(len(current_stacked_horse_map)):
            print(current_stacked_horse_map[i])

        turn_count += 1

    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다