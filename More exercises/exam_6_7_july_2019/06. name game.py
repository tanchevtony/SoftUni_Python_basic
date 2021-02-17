player_name = input()

max_points = 0
name = ''
while player_name != "Stop":
    current_points = 0

    for letters in player_name:
        number = int(input())
        if letters == chr(number):
            current_points += 10
        else:
            current_points += 2
        if current_points >= max_points:
            max_points = current_points
            name = player_name
    player_name = input()
print(f"The winner is {name} with {max_points} points!")