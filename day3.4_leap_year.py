print("Welcome to the Leap Year check!")
year = int(input("Enter the year you want to check: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print(f"Your year you want to check {year} is a Leap Year!")
        else: 
            print(f"Your year you want to check {year} is not a Leap Year!")
    else: 
        print(f"Your year you want to check {year} is a Leap Year!")
else:
     print(f"Your year you want to check {year} is not a Leap Year!")