# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# 👇 Code 👇
print("Welcome to the tip calculator.")
Bill = float(input("What was the total bll? "))
Tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
Percentage_of_tip = float(Tip / 100)
People = int(input("How many people to split the bill? "))
Total_bill = ((Bill * Percentage_of_tip) + Bill) / People
Total_amount = round(Total_bill,2)
Final_amount = "{:.2f}".format(Total_amount)
print(f"Each person should pay: {Total_bill}")
