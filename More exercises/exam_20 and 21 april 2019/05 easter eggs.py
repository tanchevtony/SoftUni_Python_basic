number_of_eggs = int(input())
red = 0
orange = 0
blue = 0
green = 0

for i in range(1, number_of_eggs + 1):
    colour = input()
    if colour == "red":
        red += 1
    elif colour == "orange":
        orange += 1
    elif colour == "blue":
        blue += 1
    elif colour == "green":
        green += 1

max_eggs_count = red
max_colour = "red"
if orange > max_eggs_count:
    max_eggs_count = orange
    max_colour = "orange"
if blue > max_eggs_count:
    max_eggs_count = blue
    max_colour = "blue"
if green > max_eggs_count:
    max_eggs_count = green
    max_colour = "green"

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_eggs_count} -> {max_colour}")
