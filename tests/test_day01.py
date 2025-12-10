from src.aoc2025.days.day01 import part01, part02
from src.aoc2025.utils import input_util

def get_input():
    return input_util.read_input("01", "dev")

def test_part_one():
    assert part01(get_input()) == 1, f"Ожидалось 42, получено {result}"

def test_part_two():
    assert part02(get_input()) == 2, f"Ожидалось 100, получено {result}"
