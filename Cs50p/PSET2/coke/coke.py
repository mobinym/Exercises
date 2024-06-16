def coke_machine():
    total = 0
    while total < 50:
        coin = int(input("Insert Coin: "))
        if coin in [5, 10, 25]:
            total += coin
            due = 50 - total if total < 50 else 0
            print(f"Amount Due: {due}")
        else:
            print(f"Amount Due: {50 - total}")
    return f"Change Owed: {total - 50 if total > 50 else 0}"

print(coke_machine())
