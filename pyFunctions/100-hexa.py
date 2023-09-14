def hexacode(userInput):
    try:
        hex_value = ''.join(hex(ord(char))[2:] for char in userInput)
        return hex_value
    except TypeError:
        return "Invalid input"

user_input = input("Enter a text: ")
hexadecimal = hexacode(user_input)
print(f"Hexadecimal is : {hexadecimal}")
   
