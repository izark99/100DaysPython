print("Welcome to FizzBuzz from 0 to your choose number!")
end_number = int(input("Enter your number: "))

for i in range(1, end_number):
    if i % 3 == 0 and i % 5 == 0:
        print(f"FizzBuzz")
    elif i % 3 == 0:
        print(f"Fizz")
    elif i % 5 == 0:
        print(f"Buzz")
    else:
        print(i)
