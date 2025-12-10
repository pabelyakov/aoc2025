from src.aoc2025.days.day01 import part01, part02
from src.aoc2025.utils import input_util

def get_input():
    return input_util.read_input("01", "dev")

def test_part_one():
    result = part01(get_input()) 
    assert result == 3, f"Ожидалось 3, получено {result}"

def test_part_two():
    result = part02(get_input()) 
    assert result == 2, f"Ожидалось 2, получено {result}"
