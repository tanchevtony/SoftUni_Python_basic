player_name = input()
start_points = 301
failed = 0
successful = 0

area = input()
while area != "Retire":
    points = int(input())

    if area == "Single":
        if points <= start_points:
            successful += 1
            start_points -= points
        else:
            failed += 1
    elif area == "Double":
        points *= 2
        if points <= start_points:
            successful += 1
            start_points -= points
        else:
            failed += 1

    elif area == "Triple":
        points *= 3
        if points <= start_points:
            successful += 1
            start_points -= points
        else:
            failed += 1

    if start_points <= 0:
        break
    area = input()
if area == "Retire":
    print(f"{player_name} retired after {failed} unsuccessful shots.")
else:
    print(f"{player_name} won the leg with {successful} shots.")


