import re

def camel_to_snake(name):
    """
    Convert camel case to snake case.
    """
    # Replace all characters that are not a word character with an underscore
    name = re.sub(r'\W+', '_', name)
    # Replace all uppercase letters with an underscore followed by the lowercase version of the letter
    name = re.sub(r'([a-z])([A-Z])', r'\1_\2', name)
    # Convert to lowercase
    name = name.lower()
    return name

# Prompt the user for input
camel_case_name = input("Enter a variable name in camel case: ")

# Convert to snake case
snake_case_name = camel_to_snake(camel_case_name)

# Output the result
print(snake_case_name)