myString = "Python is a cool program"
a_codes = " ".join([format(ord(char), '08b') for char in myString])
print(a_codes)
