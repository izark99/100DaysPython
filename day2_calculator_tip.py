print("Welcome to tip calculator tip")
total_bill = float(input("What was the total bill? "))
total_people = int(input("How many people to split the bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12, 15 "))
total_tip = tip / 100 * total_bill
total_bill_and_tip = total_bill + total_tip
bill_per_person = round(total_bill_and_tip / total_people, 2)
print(f"Each person should pay: {bill_per_person}")
