# #Under 18.5 they are underweight
# #Over 18.5 but below 25 they have a normal weight
# #Over 25 but below 30 they are slightly overweight
# #Over 30 but below 35 they are obese
# #Above 35 they are clinically obese.
# 👇Code 👇
height = float(input("Enter your height in M: "))
weight = float(input("Enter your weight in KG: "))
BMI = round(weight/(height*height))
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
elif BMI > 35:
    print(f"Your BMI is {BMI}, you are clinically obese.")
