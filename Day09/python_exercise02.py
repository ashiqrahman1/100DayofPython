student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
for marks in student_scores:
    if student_scores[marks] >= 90:
        student_grades[marks] = "Outstanding"
    elif student_scores[marks] >= 81 and student_scores[marks] <= 90:
        student_grades[marks] = "Exceeds Expectations"
    elif student_scores[marks] >= 71 and student_scores[marks] <= 80:
        student_grades[marks] = "Acceptable"
    elif student_scores[marks] <= 70:
        student_grades[marks] = "Fail"
print(student_grades)
