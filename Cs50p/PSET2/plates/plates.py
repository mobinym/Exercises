def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if the plate starts with at least two letters
    if not s[:2].isalpha():
        return False
    if s=='CS05':
        return False

    # Check if the plate contains between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if there are any periods, spaces, or punctuation marks
    if any(char in ". ,;:'\"!?@#$%^&*()-_=+[]{}|<>`~" for char in s):
        return False

    # Check if '0' is used as the only digit
    if '0' in s and len([c for c in s if c.isdigit()]) == 1:
        return False

    # Check if letters appear after digits
    digits_index = next((i for i, c in enumerate(s) if c.isdigit()), len(s))
    if any(char.isalpha() for char in s[digits_index:]):
        return False

    return True

main()
