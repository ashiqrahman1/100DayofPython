print("Welcome to BMI Calculator")
height = float(input("Enter your height in m : "))
weight = float(input("Enter your Weight in kg :"))

bmi = round(weight / (height ** 2))

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal")
elif bmi >= 25 and bmi < 30:
    print("Slightly Overweight")
elif bmi >= 30 and bmi < 35:
    print("obese")
elif bmi >= 35:
    print("Clinically Obese")
