def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"


first_name = input("Enter Your Name : ")
last_name = input("Enter Your Last Name : ")
formatedName = format_name(first_name, last_name)
print(formatedName)
