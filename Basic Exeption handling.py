# Basic exception handling

def divide_numbers():
    try:
        num1 = int(input("Enter the first number to divide: "))
        num2 = int(input("Enter the second number to divide: "))
        division = num1 / num2
        print("The result of the division is:", division)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    except ValueError:
        print("Error: Please enter valid integers.")
    finally:
        print("This is the final message, regardless of whether an exception occurs.")

# Call the function
divide_numbers()
