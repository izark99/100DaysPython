def prime_check(number):
    is_prime = True
    for i in range(2, number-1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is prime number!")
    else:
        print(f"{number} is not prime number!")

number_choose_by_user = int(input("Enter number you want to check: "))
prime_check(number_choose_by_user)