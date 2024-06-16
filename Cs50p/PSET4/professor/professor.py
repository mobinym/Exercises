import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level), generate_integer(level)
        for _ in range(3):
            guess = input(f"{x} + {y} = ")
            if guess.isdigit() and int(guess) == x + y:
                score += 1
                break
            else:
                print("EEE")
        else:
            print(f"{x} + {y} = {x + y}")
    print(f"Your score: {score}")

def get_level():
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            return int(level)
        else:
            print("Invalid level. Please enter 1, 2, or 3.")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Level must be 1, 2, or 3.")

if __name__ == "__main__":
    main()
