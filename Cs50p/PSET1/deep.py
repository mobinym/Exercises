
answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip()

if answer.lower() in ["42","forty-two", "forty two"]:
    print("Yes")
else:
    print("No")