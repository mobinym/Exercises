def main():
    # Create a dictionary with fruit names as keys and calories as values
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "sweet cherries": 100,
        "kiwifruit": 90,
        "pear": 100
        # Add other fruits and their calorie information here
    }

    # Prompt the user to input a fruit name
    fruit = input("Enter a fruit: ").lower()

    # Check if the fruit is in the dictionary
    if fruit in fruit_calories:
        print(f"Calories: {fruit_calories[fruit]}")

main()
