# You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# The highest score in the class is: x


# input value from users
student_marks = input("Enter The Students Marks : ").split()

#  convert str to int
for i in range(0, len(student_marks)):
    student_marks[i] = int(student_marks[i])

# get the max value from the list
largest_value = 0
for x in student_marks:
    if x > largest_value:
        largest_value = x

print(largest_value)
