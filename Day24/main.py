with open("./Letters/Starting_letter.txt", "r") as file:
    data = file.read()

# replace the value
with open("./Names/invited_names.txt") as name:
    for i in name:
        new_name = i.strip()
        new_data = data.replace("[Name]", new_name)
        with open(f"./Output/output_{new_name}.txt", "w") as f:
            f.write(new_data)
