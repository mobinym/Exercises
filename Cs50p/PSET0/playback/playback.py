def playback(sentence):
    return sentence.replace(' ', '...')

# Test the function
print(playback("This is CS50"))  # This...is...CS50
print(playback("This is our week on functions"))  # This...is...our...week...on...functions
print(playback("Let's implement a function called hello"))  # Let's...implement...a...function...called...hello
