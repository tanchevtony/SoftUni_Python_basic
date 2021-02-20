import math
height = int(input())
width = int(input())
percent = int(input())

total_square = height * width * 4
total_for_paint = math.ceil(total_square - (total_square * percent / 100))

paint_litres = input()
while paint_litres != "Tired!":
    total_for_paint -= int(paint_litres)

    if total_for_paint <= 0:
        break
    paint_litres = input()

if total_for_paint > 0:
    print(f"{total_for_paint} quadratic m left.")
elif total_for_paint == 0:
    print(f"All walls are painted! Great job, Pesho!")
else:
    print(f"All walls are painted and you have {abs(total_for_paint)} l paint left!")