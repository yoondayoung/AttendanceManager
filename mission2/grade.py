from mission2.enums import Grade


class GradeData:
    gold_point_ = 50
    silver_point_ = 30

    def __init__(self):
        self.grade_ = Grade.NORMAL

    def update_grade_data(self, point: int) -> Grade:
        if point >= self.gold_point_:
            self.grade_ = Grade.GOLD
        elif point >= self.silver_point_:
            self.grade_ = Grade.SILVER
        else:
            self.grade_ = Grade.NORMAL

    def is_grade_for_removal(self):
        return self.grade_ == Grade.NORMAL

    def __str__(self):
        return self.grade_.name
