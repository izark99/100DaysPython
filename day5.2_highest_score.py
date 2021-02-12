student_scores = input("Input a list of student scores: ").split()
highest_score = 0
for score in student_scores:
    if int(score) > highest_score:
        highest_score = int(score)
print(f"Highest score: {highest_score}")