from collections import Counter

def main():
    grocery_list = Counter()

    while True:
        try:
            item = input().lower()
            grocery_list[item] += 1
        except EOFError:
            break

    for item, count in sorted(grocery_list.items()):
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
