import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

str_names = str(input("Give me everybody's names: "))
names = str_names.replace(' ', '').split(',')
random_choice = random.randint(0, len(names)-1)
print(f"{names[random_choice]} will pay the bill!")