from src.aoc2025.utils import input_util

DAY_NUMBER = '01'

max_point = 99
min_point = 0

def calc_point_part_01(current_point: int, instruction):

    instr_count = int(instruction[1:])
    if instruction[0:1] == 'L':
        instr_count = instr_count * -1
    
    range_size = max_point - min_point + 1
    return (current_point - min_point + instr_count) % range_size + min_point

def part01(input: str) -> int:
    instructions = input.split("\n")
    zero_point_count = 0
    current_point = 50

    for instruction in instructions:
        current_point = calc_point_part_01(current_point=current_point, instruction=instruction)
        if current_point == 0:
            zero_point_count = zero_point_count + 1

    return zero_point_count;

# TODO
def part02(input: str) -> int:
   return 0;

def main():
    input = input_util.read_input(DAY_NUMBER, "prod")
    print(f"Day {DAY_NUMBER} Part 01: {part01(input=input)}")
    print(f"Day {DAY_NUMBER} Part 02: {part02(input=input)}")

if __name__ == "__main__":
    main()