def remove_vowels():
    text = input("Enter your text: ")
    vowels = "aeiouAEIOU"
    result = "".join([char for char in text if char not in vowels])
    return result

print(remove_vowels())
