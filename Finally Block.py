# Finally Block
def read_file(file_name):
    try:
        # Attempt to open the file
        file = open(file_name, 'r')
        
        # Read the contents of the file
        content = file.read()
        print("File content:\n", content)
    
    # Handle the case where the file is not found
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    
    # Catch any other unexpected errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    # The finally block ensures the file is closed no matter what
    finally:
        try:
            file.close()
            print("File closed.")
        except NameError:
            print("No file to close.")

# Call the function with the file name
read_file("example.txt")
