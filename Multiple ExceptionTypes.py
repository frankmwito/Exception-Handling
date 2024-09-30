#   Multiple exception types
import math

def arithmetic():
    try:
        # Input an integer value
        value = int(input("Enter an integer value: "))
        
        # Perform an arithmetic operation (raising value to the power of itself)
        power = math.pow(value, value)
        
        # Print the result
        print(f"The result of {value} raised to the power of {value} is: {power}")
    
    # Handle the case where input is not an integer
    except ValueError:
        print("ValueError: The input is not an integer. Please enter a valid integer.")
    
    # Handle other types of exceptions (TypeError, etc.)
    except TypeError:
        print("TypeError: Invalid operation with the provided input.")
    
    # Catch any other unexpected exceptions
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
arithmetic()
