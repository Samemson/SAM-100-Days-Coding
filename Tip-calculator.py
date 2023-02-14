#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
total_bill = input("What was the total bill $")
tip_percent = input("What percentage tip will you like to give? 10, 12, 15, or 20? ")
split_bill = input("How many people are to split the bill? ")
total_bills = float(total_bill)
tip_percents = float(tip_percent)
split_bills = float(split_bill)

percent = round(tip_percents / 100, 2)
percent = float(percent)
percentage = round(percent * total_bills + total_bills , 2)

people_to_split_bill = round(percentage / split_bills, 2)

print(f"Each person should pay ${people_to_split_bill}")