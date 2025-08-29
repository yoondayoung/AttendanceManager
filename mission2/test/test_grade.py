from mission2.enums import Grade
from mission2.grade import GradeData


def test_update_grade_data():
    grade = GradeData()
    grade.update_grade_data(50)
    assert grade.grade_ == Grade.GOLD


def test_is_grade_for_removal():
    grade = GradeData()
    assert grade.is_grade_for_removal() is True
