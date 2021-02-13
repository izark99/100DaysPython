print("Welcome to Pizza Order")
bill = 0
size = input("Enter your size you want to order? S or M or L: ")
add_pepperoni = input("Do you want to add pepperoni? Y or N: ")
if size.upper() == "S": 
    bill += 15
    if add_pepperoni.upper() == "Y":
        bill += 2
    print(f"Your bill is ${bill}")
elif size.upper() == "M": 
    bill += 20
    if add_pepperoni.upper() == "Y":
        bill += 3
    print(f"Your bill is ${bill}")
else: 
    bill +=25
    if add_pepperoni.upper() == "Y":
        bill += 3
    print(f"Your bill is ${bill}")



