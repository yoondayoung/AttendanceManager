import pytest

from mission2.attendance import AttendanceSystem


def test_add_new_player():
    system = AttendanceSystem()
    system.add_new_player("Eddy", "monday")
    assert system.get_players_data()["Eddy"].points_ == 1


def test_get_players_data():
    system = AttendanceSystem()
    system.add_new_player("Eddy", "monday")
    assert len(system.get_players_data()) == 1


def test_print_removed_players(capsys):
    system = AttendanceSystem()
    system.add_new_player("Eddy", "monday")
    system.print_removed_players()
    captured = capsys.readouterr()
    assert captured.out == "\nRemoved player\n==============\nEddy\n"


def test_update_players_from_file_error():
    with pytest.raises(FileNotFoundError):
        system = AttendanceSystem()
        system.update_players_from_file('aaa.txt')


def test_regression_attendance_system(capsys):
    expected_values = '''NAME : Umar, POINT : 48, GRADE : SILVER
NAME : Daisy, POINT : 45, GRADE : SILVER
NAME : Alice, POINT : 61, GRADE : GOLD
NAME : Xena, POINT : 91, GRADE : GOLD
NAME : Ian, POINT : 23, GRADE : NORMAL
NAME : Hannah, POINT : 127, GRADE : GOLD
NAME : Ethan, POINT : 44, GRADE : SILVER
NAME : Vera, POINT : 22, GRADE : NORMAL
NAME : Rachel, POINT : 54, GRADE : GOLD
NAME : Charlie, POINT : 58, GRADE : GOLD
NAME : Steve, POINT : 38, GRADE : SILVER
NAME : Nina, POINT : 79, GRADE : GOLD
NAME : Bob, POINT : 8, GRADE : NORMAL
NAME : George, POINT : 42, GRADE : SILVER
NAME : Quinn, POINT : 6, GRADE : NORMAL
NAME : Tina, POINT : 24, GRADE : NORMAL
NAME : Will, POINT : 36, GRADE : SILVER
NAME : Oscar, POINT : 13, GRADE : NORMAL
NAME : Zane, POINT : 1, GRADE : NORMAL

Removed player
==============
Bob
Zane
'''
    system = AttendanceSystem()
    system.update_players_from_file("attendance_weekday_500.txt")
    system.print_attendance_system()
    captured = capsys.readouterr()
    assert captured.out == expected_values
