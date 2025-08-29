import pytest

from mission2.enums import get_day_enum


def test_get_day_enum():
    with pytest.raises(ValueError):
        day = get_day_enum('weddnesday')
