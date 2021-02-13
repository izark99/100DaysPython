import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

your_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if your_choose > 2 or your_choose < 0:
    print("You type wrong number! So I choose random for you")
    your_choose = random.randint(0,2)
    if your_choose == 0:
        print(rock)
    elif your_choose == 1:
        print(paper)
    else:
        print(scissors)
elif your_choose == 0:
    print(rock)
elif your_choose == 1:
    print(paper)
elif your_choose == 2:
    print(scissors)

print("Computer choose: ")
ramdom_choose = random.randint(0,2)
if ramdom_choose == 0:
    print(rock)
elif ramdom_choose == 1:
    print(paper)
else:
    print(scissors)

if your_choose == 0 and ramdom_choose == 2:
    print("You win!")
elif ramdom_choose > your_choose:
    print("You lose!")
elif ramdom_choose < your_choose:
    print("You win!")
elif ramdom_choose == your_choose:
    print("Draw!")
else:
    print("You lose!")
