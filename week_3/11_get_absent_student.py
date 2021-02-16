all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    dict = {}
    for key in all_students:  # O(N)
        dict[key] = True  # 공간 복잡도 O(N) 만큼의 추가 공간 필요

    for key in present_array:  # O(N)
        del dict[key]

    return list(dict.keys())

print(get_absent_student(all_students, present_students))