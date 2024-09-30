# Raise exception manually

def check_voting_eligibility():
    try:
        # Prompt user to enter their age
        age = int(input("Enter your age: "))

        # Raise exceptions based on age input
        if age < 0:
            raise ValueError("Age cannot be negative.")
        elif age < 18:
            raise ValueError("You are not eligible to vote.")
        else:
            print("You are eligible to vote.")

    except ValueError as ve:
        # Handle ValueError for invalid ages (below 18 or negative numbers)
        print(f"ValueError: {ve}")
    except TypeError as te:
        # Handle TypeError for incorrect input types
        print(f"TypeError: {te}")
    except Exception as e:
        # Catch any other exceptions
        print(f"An unexpected error occurred: {e}")

# Call the function to check voting eligibility
check_voting_eligibility()

