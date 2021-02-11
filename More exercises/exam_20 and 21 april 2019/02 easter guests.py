import math

guests = int(input())
budget = int(input())

easter_bread = 4
eggs = 0.45

number_of_easter_breads = math.ceil(guests / 3)
number_of_eggs = math.ceil(guests * 2)

easter_bread_price = number_of_easter_breads * easter_bread
eggs_price = number_of_eggs * eggs
total = easter_bread_price + eggs_price
difference = abs(total - budget)

if budget >= total:
    print(
        f"Lyubo bought {number_of_easter_breads} Easter bread and {number_of_eggs} eggs.\nHe has {difference:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.\nHe needs {difference:.2f} lv. more.")
