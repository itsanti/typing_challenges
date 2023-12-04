from constants import ___
from typing import Callable

def create_user(user_name: str, user_age: int, after_created: Callable[[int], None]) -> None:
    return None


def send_test_email(user_id: int) -> None:
    return None


if __name__ == "__main__":
    create_user(
        user_name="Ilya",
        user_age=32,
        after_created=send_test_email,
    )
