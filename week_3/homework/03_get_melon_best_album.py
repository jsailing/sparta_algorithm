genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    play_by_genre_dict = {}
    index_play_array_by_genre_dict = {}
    for i in range(len(genre_array)):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in play_by_genre_dict:
            play_by_genre_dict[genre] = play
            index_play_array_by_genre_dict[genre] = [(i, play)]
        else:
            play_by_genre_dict[genre] += play
            index_play_array_by_genre_dict[genre].append((i, play))

    sorted_genre_play_array = sorted(play_by_genre_dict.items(), key=lambda item: item[1], reverse=True)
    result = []
    for genre, _ in sorted_genre_play_array:
        index_play_array = index_play_array_by_genre_dict[genre]
        sorted_index_play_array = sorted(index_play_array, key=lambda item: (item[1], item[0]), reverse=True)
        print(sorted_index_play_array)
        for i in range(len(sorted_index_play_array)):
            if i > 1:
                break
            result.append(sorted_index_play_array[i][0])

    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
