import pytest

from mission2.player import Player


def test_update_data():
    p = Player('Alice', 'tuesday')
    p.update_data('wednesday')
    assert p.points_ == 4


def test_get_weekend_attendance():
    p = Player('Alice', 'tuesday')
    p.update_data('saturday')
    assert p.get_weekend_attendance() == 1


def test_calculate_bonus_points():
    p = Player('Alice', 'wednesday')
    for _ in range(20):
        p.update_data('wednesday')
    p.calculate_bonus_points()
    assert p.points_ == 73


def test_update_grade():
    p = Player('Alice', 'wednesday')
    for _ in range(20):
        p.update_data('wednesday')
    p.calculate_bonus_points()
    p.update_grade()
    assert str(p.grade_) == 'GOLD'
