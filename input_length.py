# Task 1: Input Data Validator

def input_length_validator():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    if len(first_name) < 2 or len(last_name) < 2:
        print("Error: Both first name and last name must be at least 2 characters long.")
    else:
        print("Valid input!")

input_length_validator()