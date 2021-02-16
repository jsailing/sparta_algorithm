from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

# game_map = [
#     ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
#     ["#", "R", "#", ".", ".", ".", "#", "#", "B", "#"],
#     ["#", ".", ".", ".", "#", ".", "#", "#", ".", "#"],
#     ["#", "#", "#", "#", "#", ".", "#", "#", ".", "#"],
#     ["#", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
#     ["#", ".", "#", "#", "#", "#", "#", "#", ".", "#"],
#     ["#", ".", "#", ".", ".", ".", ".", "#", ".", "#"],
#     ["#", ".", "#", ".", "#", ".", "#", ".", ".", "#"],
#     ["#", ".", ".", ".", "#", ".", "O", "#", ".", "#"],
#     ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
# ]  # -> False 를 반환해야 한다

#    ←, →, ↑, ↓
dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]

def move_until_wall_or_hole(r, c, d, game_map):
    move_count = 0
    while game_map[r + dr[d]][c + dc[d]] != "#" and game_map[r][c] != "O":
        r += dr[d]
        c += dc[d]
        move_count += 1

    return r, c, move_count


def is_available_to_take_out_only_red_marble(game_map):
    n, m = len(game_map), len(game_map[0])
    # visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    red_visited = [[False] * m for _ in range(n)]
    blue_visited = [[False] * m for _ in range(n)]

    queue = deque()
    red_row, red_col, blue_row, blue_col = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_row, red_col = i, j
            elif game_map[i][j] == "B":
                blue_row, blue_col = i, j

    queue.append((red_row, red_col, blue_row, blue_col, 1))
    # visited[red_row][red_col][blue_row][blue_col] = True
    red_visited[red_row][red_col] = True
    blue_visited[blue_row][blue_col] = True
    print(queue[0])

    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()
        if try_count > 20:
            break

        for i in range(4):  # 4 directions
            next_red_row, next_red_col, r_count = move_until_wall_or_hole(red_row, red_col, i, game_map)
            next_blue_row, next_blue_col, b_count = move_until_wall_or_hole(blue_row, blue_col, i, game_map)
            print(next_red_row, next_red_col, next_blue_row, next_blue_col)

            if game_map[next_blue_row][next_blue_col] == "O":
                continue
            elif game_map[next_red_row][next_red_col] == "O":
                return True

            # if next_red_row == next_blue_row and next_red_col == next_blue_col:
            if (next_red_row, next_blue_row) == (next_blue_row, next_blue_col):
                if r_count > b_count:
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]

            # if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
            #     visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
            if not red_visited[next_red_row][next_red_col] or not blue_visited[next_blue_row][next_blue_col]:
                red_visited[next_red_row][next_red_col] = True
                blue_visited[next_blue_row][next_blue_col] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))

    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다