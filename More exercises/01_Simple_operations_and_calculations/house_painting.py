x = float(input())
y = float(input())
h = float(input())

windows = (1.5 * 1.5) * 2
door = 1.2 * 2
side_square = ((x * x) * 2) - door
side_rectangle = ((x * y) * 2) - windows
roof_side = (x * y) * 2
roof_front = (x * h / 2) * 2
total_house = (side_square + side_rectangle) / 3.4
total_roof = (roof_side + roof_front) / 4.3

print(f"{total_house:.2f}")
print(f"{total_roof:.2f}")