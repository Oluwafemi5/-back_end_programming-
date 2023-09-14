def calc(num1, num2, sign):
    if sign == '+':
        result = num1 + num2
    elif sign == '-':
        result = num1 - num2
    elif sign == '*':
        result = num1 * num2
    elif sign == '/':
        if num2 == 0:
            result = "Cannot divide by zero"
        else:
            result = num1 / num2
    elif sign == '%':
        result = num1 % num2
    else:
        result = "Invalid operator"

    return result

while True:
    try:
        input_str = input("Enter an expression (e.g., 1 + 2): ")
        if input_str.lower() == "quit":
           
        Pons = input_str.split()
        num1 = int(Pons[0])
        sign = Pons[1]
        num2 = int(Pons[2])

        result = calc(num1, num2, sign)
        print(f"The Result of {num1} and {num2} is : {result}")
    except ValueError:
        print("Invalid input. Please use the format 'number operator number'.")
    except ZeroDivisionError:
        print("Cannot be divided.")
        
