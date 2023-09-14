def Ascii_value():
    value = input(" Enter your words: ")
    A_SC = " ".join([format(ord(char), '08b') for char in value])
    print(f"The ASCII value of '{value}' is {A_SC} ")
Ascii_value()
