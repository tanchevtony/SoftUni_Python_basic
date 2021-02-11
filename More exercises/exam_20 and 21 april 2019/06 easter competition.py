number_of_bake = int(input())

top_baker_name = ''
max_points = 0
for i in range(1, number_of_bake + 1):
    name = input()
    current_name = name
    current_points = 0
    points = input()
    while points != "Stop":
        points = int(points)
        current_points += points
        points = input()
    print(f"{name} has {current_points} points.")

    if current_points > max_points:
        max_points = current_points
        top_baker_name = name
        print(f"{top_baker_name} is the new number 1!")
print(f"{top_baker_name} won competition with {max_points} points!")