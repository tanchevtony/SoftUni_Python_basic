import math
height = int(input())
width = int(input())
percent = int(input())
litres = 0
total_square = math.ceil(height * width * 4)
total_for_paint = total_square - total_square * percent / 100

paint_litres = input()
while paint_litres != "Tired!":
    paint_litres = int(paint_litres)
    litres += paint_litres
    if total_for_paint < 0:
        break
    else:
        total_for_paint -= paint_litres
    paint_litres = input()
if total_for_paint < litres:
    difference =
print(f"{}")
