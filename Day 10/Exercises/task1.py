# def format_name(f_name, l_name):
#     first_name = f_name.lower()
#     first_name = first_name[0].upper() + first_name[1:]
#     last_name = l_name.lower()
#     last_name = last_name[0].upper() + last_name[1:]
    
#     return first_name + " " + last_name

def format_name(f_name, l_name):
    format_f_name = f_name.title()
    format_l_name = l_name.title()

    return f"{format_f_name} {format_l_name}"

print(format_name("haRRIson", "pAyeSa"))