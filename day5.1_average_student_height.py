student_heights = input("Input a list of student heights: ").split()
total_student_height = 0
for height in student_heights:
    total_student_height += int(height)
average_student_height = total_student_height/len(student_heights)
print(f"Average student height: {round(average_student_height, 2)}")