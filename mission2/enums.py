from enum import Enum


class Day(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6

    def __get__(self, *args):
        return int(self.value)


class Grade(Enum):
    GOLD = 1
    SILVER = 2
    NORMAL = 0


def get_day_enum(day: str) -> Day:
    if day == 'monday':
        return Day.Monday
    elif day == 'tuesday':
        return Day.Tuesday
    elif day == 'wednesday':
        return Day.Wednesday
    elif day == 'thursday':
        return Day.Thursday
    elif day == 'friday':
        return Day.Friday
    elif day == 'saturday':
        return Day.Saturday
    elif day == 'sunday':
        return Day.Sunday
    raise ValueError("invalid day value")
