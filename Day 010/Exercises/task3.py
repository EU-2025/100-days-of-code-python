def format_name(f_name, l_name):
    """Take a first and last anem and format it to return the
    title case version of the name."""
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    format_f_name = f_name.title()
    format_l_name = l_name.title()

    return f"Result: {format_f_name} {format_l_name}"

print(format_name(input("What is your first name? "), input("What is your lastname? ")))