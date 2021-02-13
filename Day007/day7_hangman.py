import random

word_list = ['money', 'python', 'handsome']

keyword = random.choice(word_list)
end_game = False
heart = 5
display = []
for letter in keyword:
    display += "_"
print(keyword)
print("Welcome to HANGMAN game!")
print(f'{" ".join(display)}')
while not end_game:
    guess = input("\nGuess a letter: ").lower()
    for i in range(len(keyword)):
        letter = keyword[i]
        if guess == letter:
            display[i] = letter
    print(f'{" ".join(display)}')
    if guess not in keyword:
        heart = heart - 1
        if heart >= 1:
            print(f"Your heart is {heart}")
        else:
            end_game = True
            print("You lose!")
    if "_" not in display:
        end_game = True
        print("You win!")

