PLACE_HOLDER = "[name]"

names = []

# Read the names
# with open(r"Input\Names\invited_names.txt") as file:
#     name_list = file.readlines()
#     for line in name_list:
#         if line != name_list[-1]:
#             names.append(line[:-1])
#         else:
#             names.append(line)
            
with open(r"Input\Names\invited_names.txt") as file:
    name_list = file.readlines()
    for line in name_list:
        names.append(line.strip())
            
# Write a letter for each name
# def write_letter(name):
#     new_text = ""
#     with open(r"Input\Letters\starting_letter.txt", "r") as file:
#         text = file.readlines()
#         new_line = text[0].replace(PLACE_HOLDER, name)
#         new_text += new_line
#         for line in text[1:]:
#             new_text += line
#         if " " in name:
#             name = name.replace(" ", "_")
#     file_path = f"Output\ReadyToSend\Letter_for_{name}"
#     with open(file_path, "w") as file:
#         file.write(new_text) 

def write_letter(name):
    with open(r"Input\Letters\starting_letter.txt", "r") as file:
        text = file.read()
        new_text = text.replace(PLACE_HOLDER, name)
        if " " in name:
            name = name.replace(" ", "_")
    file_path = f"Output\ReadyToSend\Letter_for_{name}.txt"
    with open(file_path, "w") as file:
        file.write(new_text)  


for name in names:
    write_letter(name)