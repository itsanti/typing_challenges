from constants import ___

Point = tuple[int, int]

def is_point_in_square(point: Point, left_upper_corner: Point, right_bottom_corner: Point) -> bool:
    return True


if __name__ == "__main__":
    assert is_point_in_square(
        point=(10, 12),
        left_upper_corner=(5, 5),
        right_bottom_corner=(20, 15)
    ) is True
