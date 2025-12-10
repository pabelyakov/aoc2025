import os

def read_input(day: str, env: str)-> str:
    day_file = f"day{day}.txt"
    day_path = os.path.join("resources", env, day_file)
    
    with open(day_path, 'r') as file:
        return file.read().strip()