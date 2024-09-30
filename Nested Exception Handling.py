# Nested exception handling

def nested_exception():
    try:
        # Division operation
        num1 = int(input("Enter the first number for division: "))
        num2 = int(input("Enter the second number for division: "))
        division = num1 / num2
        print("Division result: ", division)
    except ValueError as ve:
        print("Error: Invalid input. Please enter a valid number.", ve)
    except TypeError as te:
        print("Error: Type error occurred.", te)
    except ZeroDivisionError as zde:
        print("Error: Division by zero is not allowed.", zde)
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Nested exception block for list operations
    try:
        num_list = []
        num = int(input("Enter the size of the list: "))
        for i in range(num):
            numbers = int(input(f"Enter number at index {i+1}: "))
            num_list.append(numbers)
        print(num_list[int(input("Enter index to retrieve value: "))])
    except IndexError as ie:
        print("Error: List index out of range.", ie)
    except ValueError as ve:
        print("Error: Invalid input. Please enter a valid number.", ve)
    
    # Nested exception block for dictionary operations
    try:
        num_dict = {}
        num = int(input("Enter the size of your dictionary: "))
        for i in range(num):
            name = input(f"Enter name for key {i+1}: ")
            age = int(input(f"Enter age for key {i+1}: "))
            num_dict[name] = age  # Proper dictionary update
        print(num_dict.get(input("Enter the key to search in dictionary: ")))
    except KeyError as ke:
        print("Error: Key not found in the dictionary.", ke)
    except ValueError as ve:
        print("Error: Invalid input. Please enter a valid number.", ve)

# Call the function to test nested exception handling
nested_exception()
