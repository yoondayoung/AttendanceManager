from mission2.enums import Day, get_day_enum
from mission2.grade import GradeData

BONUS_POINT = 10
DAYS_MIN_FOR_BONUS_POINT = 10


class Player:
    def __init__(self, name, day):
        self.name = name
        self.attendance_ = [0] * 7
        self.points_ = 0
        self.grade_ = GradeData()
        self.update_data(day)

    @staticmethod
    def calculate_basic_points(day):
        add_point = 1
        if day == Day.Wednesday:
            add_point = 3
        elif day == Day.Saturday:
            add_point = 2
        elif day == Day.Sunday:
            add_point = 2
        return add_point

    def update_data(self, day_str):
        day = get_day_enum(day_str)
        self.attendance_[day] += 1
        self.points_ += self.calculate_basic_points(day)

    def get_weekend_attendance(self):
        return self.attendance_[Day.Saturday] + self.attendance_[Day.Sunday]

    def calculate_bonus_points(self):
        bonus_points = 0
        if self.attendance_[Day.Wednesday] >= DAYS_MIN_FOR_BONUS_POINT:
            bonus_points += BONUS_POINT
        if self.get_weekend_attendance() >= DAYS_MIN_FOR_BONUS_POINT:
            bonus_points += BONUS_POINT
        self.points_ += bonus_points

    def update_grade(self):
        self.grade_.update_grade_data(self.points_)

    def is_removed(self):
        return self.grade_.is_grade_for_removal() and self.attendance_[
            Day.Wednesday] == 0 and self.get_weekend_attendance() == 0

    def print_data(self):
        print(f"NAME : {self.name}, POINT : {self.points_}, GRADE : {self.grade_}")
