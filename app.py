def double(x):
    # Double the value x.
    return x * 2


def get_initials(full_name: str):
    # Split the name, and raise an Exception if it is invalid.
    split_names = full_name.split(" ")
    if len(split_names) != 2:
        raise Exception(f"The name '{full_name}' is invalid. It needs to be two strings, separated by a space.")
    
    # Get the first letter of each name and join them together.
    first_letter = split_names[0][0]
    last_letter = split_names[1][0]
    initials = first_letter + last_letter

    # Capitalize the results and return them.
    return initials.upper()
