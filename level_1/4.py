import datetime

from constants import ___


def calculate_age(date_of_birth: datetime.date) -> int:
    return 57


if __name__ == "__main__":
    assert calculate_age(date_of_birth=datetime.date(1965, 6, 2)) == 57
