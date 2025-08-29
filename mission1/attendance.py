import os


def add_new_player(player_id, day) -> list:
    # player_dict{'name' : [id, attendance[요일], point, grade]}
    new_player_data = [player_id, [0] * 7, 0, 0]
    return update_player(new_player_data, day)


def get_attendance_index(day: str):
    try:
        if day == "monday":
            return 0
        elif day == "tuesday":
            return 1
        elif day == "wednesday":
            return 2
        elif day == "thursday":
            return 3
        elif day == "friday":
            return 4
        elif day == "saturday":
            return 5
        elif day == "sunday":
            return 6
        else:
            raise ValueError()
    except ValueError:
        print("day 값이 invalid 합니다.")


def update_player(player_data, day) -> list:
    add_point = 1
    day_index = get_attendance_index(day)

    if day == "wednesday":
        add_point = 3
    elif day == "saturday":
        add_point = 2
    elif day == "sunday":
        add_point = 2

    player_data[1][day_index] += 1
    player_data[2] += add_point

    return player_data


def get_attendance_data_from_file(file) -> dict:
    player_dict = {}
    with open(file, encoding='utf-8') as f:
        for line in f.readlines():
            attendance = line.strip().split()
            if len(attendance) == 2:
                player_name = attendance[0]
                if player_name not in player_dict:
                    player_dict[player_name] = add_new_player(len(player_dict), attendance[1])
                else:
                    player_dict[player_name] = update_player(player_dict[player_name], attendance[1])

    return player_dict


def print_attendance_system(file):
    player_dict = {}
    try:
        if not os.path.exists(file):
            raise FileNotFoundError()

        player_dict = get_attendance_data_from_file(file)
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

    for name, data in player_dict.items():
        player_dict[name][2] += calculate_player_bonus_points(player_dict[name])
        player_dict[name][3] = get_player_grade(player_dict[name][2])

        print_grade(name, player_dict[name][2], player_dict[name][3])

    print_removed_player(player_dict)


def get_player_grade(player_point):
    if player_point >= 50:
        return 1
    elif player_point >= 30:
        return 2
    else:
        return 0


def calculate_player_bonus_points(player_data):
    bonus_point = 0
    if player_data[1][2] > 9:
        bonus_point += 10
    if get_player_weekend_attendance(player_data) > 9:
        bonus_point += 10
    return bonus_point


def get_player_weekend_attendance(player_data):
    return player_data[1][5] + player_data[1][6]


def print_removed_player(player_dict):
    print("\nRemoved player")
    print("==============")
    for player_name, data in player_dict.items():
        if is_player_removed(data):
            print(player_name)


def is_player_removed(data):
    return data[3] not in (1, 2) and data[1][2] == 0 and get_player_weekend_attendance(data) == 0


def print_grade(player_name, player_point, player_grade):
    print(f"NAME : {player_name}, POINT : {player_point}, GRADE : {get_grade_name(player_grade)}")


def get_grade_name(player_grade) -> str:
    if player_grade == 1:
        return "GOLD"
    elif player_grade == 2:
        return "SILVER"
    else:
        return "NORMAL"


if __name__ == "__main__":
    print_attendance_system("attendance_weekday_500.txt")
