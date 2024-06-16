def main():
    word = input("Enter a word: ")
    print(shorten(word))

def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return ''.join([letter for letter in word if letter not in vowels])

if __name__ == "__main__":
    main()
