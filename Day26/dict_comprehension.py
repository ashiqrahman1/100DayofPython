import random
name = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_dict = {student: random.randint(20, 80) for student in name}
print(new_dict)
student_who_pass = {key: value for (
    key, value) in new_dict.items() if value >= 60}

print(student_who_pass)
