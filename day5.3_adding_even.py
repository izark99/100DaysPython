print("Welcome to calculator even number from 0 to your choose number!")
end_number = int(input("Enter your number: "))
sum = 0
# for i in range(0, end_number):
#     if i % 2 == 0:
#         sum += i
for i in range(0, end_number, 2):
        sum += i
print(f"Result: {sum}")