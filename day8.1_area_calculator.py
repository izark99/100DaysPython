import math


def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area/cover)
    print(f"You'll need {num_of_cans} cans of print")

height_value = int(input("Height of wall: "))
width_value = int(input("Width of wall: "))
cover_value = 5

paint_calc(height_value, width_value, cover_value)
