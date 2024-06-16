def sum(num1,num2):
    return num1 + num2

def mul(num1,num2):
    return num1 * num2

def search_to_list(list1,x):
    if x in list1:
        return list1
    return False
def main():
    # Test the sum function
    print(sum(1, 2))  # Output: 3

    # Test the mul function
    print(mul(3, 4))  # Output: 12

    # Test the search_to_list function
    my_list = [1, 2, 3, 4, 5]
    print(search_to_list(my_list, 3))  # Output: [1, 2, 3, 4, 5]
    print(search_to_list(my_list, 6))  # Output: False

if __name__ == "__main__":
    main()
