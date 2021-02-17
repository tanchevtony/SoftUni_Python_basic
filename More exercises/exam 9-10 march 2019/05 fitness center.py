visitors = int(input())
back = 0
chest = 0
legs = 0
abs_people = 0
protein_shake = 0
protein_bar = 0
for i in range(1, visitors + 1):
    action = input()

    if action == "Back":
        back += 1
    elif action == "Chest":
        chest += 1
    elif action == "Legs":
        legs += 1
    elif action == "Abs":
        abs_people += 1
    elif action == "Protein shake":
        protein_shake += 1
    elif action == "Protein bar":
        protein_bar += 1
total_gym = back + chest + legs + abs_people
product = protein_bar + protein_shake
percent_gym = total_gym / visitors * 100
percent_product = product / visitors * 100

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs_people} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{percent_gym:.2f}% - work out")
print(f"{percent_product:.2f}% - protein")
100/100
