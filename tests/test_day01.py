from src.aoc2025.days.day01 import part01, part02

def test_part_one():
    """Тест для функции part_one"""
    result = part01()
    assert isinstance(result, int), "Результат должен быть целым числом"
    assert result == 1, f"Ожидалось 42, получено {result}"

def test_part_two():
    """Тест для функции part_two"""
    result = part02()
    assert isinstance(result, int), "Результат должен быть целым числом"
    assert result == 2, f"Ожидалось 100, получено {result}"
