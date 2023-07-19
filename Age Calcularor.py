age = input("What is your current age? ")
years_left = 90 - int(age)
month_left = years_left*12
days_left = years_left*365
weeks_left = years_left*52
print(f"You have {days_left} Days,{weeks_left} weeks,and {month_left} months left.")
