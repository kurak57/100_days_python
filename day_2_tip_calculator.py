print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_bill = bill+(bill*tip/100)
pay_per_person = round(total_bill/people,2)

print(f"Each person should pay: ${pay_per_person}")