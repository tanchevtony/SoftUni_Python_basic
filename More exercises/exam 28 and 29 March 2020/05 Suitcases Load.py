plane_capacity = float(input())
no_more_place = False
iterations_counter = 0
command = input()
while command != "End":
    suitcase_volume = float(command)
    iterations_counter += 1
    if iterations_counter % 3 == 0:
        suitcase_volume *= 1.1
    if plane_capacity - suitcase_volume < 0:
        iterations_counter -= 1
        no_more_place = True
        break
    plane_capacity -= suitcase_volume
    command = input()
if no_more_place:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {iterations_counter} suitcases loaded.")