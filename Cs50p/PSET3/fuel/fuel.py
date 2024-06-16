while True:
    try:
        # Prompt the user for a fraction
        fraction = input("Enter a fraction: ")
        x, y = map(int, fraction.split('/'))

        # Check if X is greater than Y or Y is 0
        if x > y or y == 0:
            continue

        # Calculate the percentage
        percentage = round(x / y * 100)

        # Output the fuel level
        if percentage <= 1:
            print("E")
            break
        elif percentage >= 99:
            print("F")
            break
        else:
            print(f"{percentage}%")
            break

    except (ValueError, ZeroDivisionError):
        # Handle exceptions and prompt the user again
        continue
