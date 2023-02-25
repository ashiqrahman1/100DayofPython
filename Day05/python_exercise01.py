# Find the Average Height of Students
student_height = input("Enter the Student Heights :").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

sum = 0
for student in student_height:
    sum += student
# Find Average
average = sum/(len(student_height))
print(round(average))
