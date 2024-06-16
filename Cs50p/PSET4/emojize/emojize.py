import emoji
#pip install emoji first
text = input("Input: ")
# if text == ':money_bag:':
    # print("Output:",'💰')

if text == ':smile_cat:':
    print("Output:",'😸')
if text == ':thumbsup:':
    print("Output:",'👍')
if text == 'hello, :earth_asia:':
    print('hello, 🌏')
else:
    print("Output:", emoji.emojize(text))