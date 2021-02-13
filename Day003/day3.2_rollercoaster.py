print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    ticketPrice = 0
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        print("Child ticket are $5.")
        ticketPrice += 5
    elif age <= 18:
        print("Youth ticket are $7.")
        ticketPrice += 7
    else:
        print("Adult ticket are $12.")
        ticketPrice += 12
    takeAPhoto = input("Do you want to take a photo while ride rollercoaster? Y or N ")
    if takeAPhoto.upper() == "Y":
        ticketPrice += 3
    print(f"Your ticket price is ${ticketPrice}")
else:
    print("Sorry! you have to grow taller before you can ride")