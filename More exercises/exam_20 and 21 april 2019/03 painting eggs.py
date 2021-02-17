eggs_size = input()
eggs_colour = input()
packs = int(input())

price = 0
if eggs_colour == "Red":
    if eggs_size == "Large":
        price = 16
    elif eggs_size == "Medium":
        price = 13
    elif eggs_size == "Small":
        price = 9
elif eggs_colour == "Green":
    if eggs_size == "Large":
        price = 12
    elif eggs_size == "Medium":
        price = 9
    elif eggs_size == "Small":
        price = 8
elif eggs_colour == "Yellow":
    if eggs_size == "Large":
        price = 9
    elif eggs_size == "Medium":
        price = 7
    elif eggs_size == "Small":
        price = 5

sum_packs = packs * price
expenses = sum_packs * 0.35
total = sum_packs - expenses
print(f"{total:.2f} leva.")