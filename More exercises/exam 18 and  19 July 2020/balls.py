number = int(input())

red_count = 0
orange_count = 0
yellow_count = 0
white_count = 0
black_count = 0
total_points = 0
other_count = 0
for i in range(1, number + 1):
    colour = input()

    if colour == "red":
        red_count += 1
        total_points += 5
    elif colour == "orange":
        orange_count += 1
        total_points += 10
    elif colour == "yellow":
        yellow_count += 1
        total_points += 15
    elif colour == "white":
        white_count += 1
        total_points += 20
    elif colour == "black":
        black_count += 1
        total_points //= 2
    else:
        other_count += 1
    continue

print(f"Total points: {total_points}")
print(f"Points from red balls: {red_count}")
print(f"Points from orange balls: {orange_count}")
print(f"Points from yellow balls: {yellow_count}")
print(f"Points from white balls: {white_count}")
print(f"Other colors picked: {other_count}")
print(f"Divides from black balls: {black_count}")
