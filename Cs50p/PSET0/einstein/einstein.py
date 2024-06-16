def calculate_energy():
    # Speed of light in meters per second
    c = 300000000

    # Prompt the user for mass
    mass = int(input("Enter mass in kilograms: "))

    # Calculate energy
    energy = mass * (c ** 2)

    # Output energy
    print(energy)

# Call the function
calculate_energy()
