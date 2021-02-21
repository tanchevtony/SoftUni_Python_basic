import math
width = float(input())
length = float(input())
high = float(input())
astronauts = float(input())

spaceship_volume = width * length * high
room_volume = (astronauts + 0.40) * 2 * 2
available_space_for = math.floor(spaceship_volume / room_volume)

if 3 <= available_space_for <= 10:
    print(f"The spacecraft holds {available_space_for} astronauts.")
elif available_space_for < 3:
    print("The spacecraft is too small.")
elif available_space_for > 10:
    print("The spacecraft is too big.")